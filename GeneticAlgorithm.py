from random import seed
from random import randint
from random import random
from random import choices

from Chromosome import Chromosome


class GeneticAlgorithm:
    """ Canonical genetic algorithm:
    - chromosome - a binary string,
    - gene       - each bit of binary size,
    - fixed population size,
    - roulette wheel selection,
    - single point crossover,
    - gene-wise mutation. """

    POPULATION_SIZE = 20
    POPULATIONS_LIMIT = 100
    CHROMOSOME_MUTATION_PROBABILITY = 0.3
    GENE_MUTATION_PROBABILITY = 0.15
    RANDOM_SEED = 1975

    # Keep starting population to compare with the resulting population
    starting_population = list()
    resulting_population = list()

    # Before adding offspring to resulting population we will save it to a separate
    # list to perform mutation
    offspring_list = list()

    def __init__(self, fitness_function):
        seed(self.RANDOM_SEED)  # random.seed()
        self.fitness_function = fitness_function
        self.create_starting_population()

        for i in range(self.POPULATIONS_LIMIT):
            self.panmixia_selection()
            self.population_crossover()
            self.mutate_population()
            self.create_new_population()

    def __str__(self):
        pass

    # Population initialization functions

    def create_individual(self):
        """ Each individual consists of two chromosomes,
        each chromosome is 1 byte long: 4 bits for integer part
        and 4 bits for fractional part. """
        x = Chromosome()
        y = Chromosome()
        individual = [x, y]
        return individual

    def create_starting_population(self):
        for i in range(self.POPULATION_SIZE):
            self.starting_population.append(self.create_individual())

        # Creating a copy of a starting population to work with it
        self.resulting_population = self.starting_population.copy()

    # Selection and breeding functions

    def panmixia_selection(self):
        """ Select individuals for breeding. """
        first_parent = self.resulting_population[
            randint(0, self.POPULATION_SIZE - 1)]
        second_parent = self.resulting_population[
            randint(0, self.POPULATION_SIZE - 1)]
        breeding_pair = [first_parent, second_parent]
        return breeding_pair

    def single_point_crossover(self, breeding_pair):
        """ Two individuals crossover.
        We exclude 0th and 9th bit of each chromosome from list of possible
        crossover points to avoid the situations when children chromosomes
        are fully identical to their parents chromosomes. """
        first_parent_x = breeding_pair[0][0].get_binary_representation()
        first_parent_y = breeding_pair[0][1].get_binary_representation()
        second_parent_x = breeding_pair[1][0].get_binary_representation()
        second_parent_y = breeding_pair[1][1].get_binary_representation()

        crossover_point_x = randint(1, 8)
        crossover_point_y = randint(1, 8)

        binary_mask_x = 256 - 2 ** crossover_point_x
        binary_mask_y = 256 - 2 ** crossover_point_y

        first_child_x = Chromosome(first_parent_x & binary_mask_x +
                                   second_parent_x & (255 - binary_mask_x))
        first_child_y = Chromosome(first_parent_y & binary_mask_y +
                                   second_parent_y & (255 - binary_mask_y))

        second_child_x = Chromosome(second_parent_x & binary_mask_x +
                                    first_parent_x & (255 - binary_mask_x))
        second_child_y = Chromosome(second_parent_y & binary_mask_y +
                                    first_parent_y & (255 - binary_mask_y))

        first_child = [first_child_x, first_child_y]
        second_child = [second_child_x, second_child_y]
        offspring = (first_child, second_child)
        return offspring

    def population_crossover(self):
        """ Perform crossover for all selected individuals. """
        for i in range(self.POPULATION_SIZE):
            breeding_pair = self.panmixia_selection()

            if breeding_pair[0] != breeding_pair[1]:
                offspring = self.single_point_crossover(breeding_pair)
                self.offspring_list.append(offspring[0])
                self.offspring_list.append(offspring[1])

    # Mutation functions

    def mutate_chromosome(self, chromosome):
        gene_mutation_probabilities = (random() for i in range(10))
        inverting_mask = 0

        for probability in gene_mutation_probabilities:
            if probability < self.GENE_MUTATION_PROBABILITY:
                inverting_mask = (inverting_mask << 1) + 1
            else:
                inverting_mask = inverting_mask << 1

        mutated_chromosome = chromosome ^ inverting_mask
        return mutated_chromosome

    def mutate_population(self):
        for individual in self.offspring_list:
            if random() < self.CHROMOSOME_MUTATION_PROBABILITY:
                x = individual[0].get_binary_representation()
                individual[0] = Chromosome(self.mutate_chromosome(x))

            if random() < self.CHROMOSOME_MUTATION_PROBABILITY:
                y = individual[1].get_binary_representation()
                individual[1] = Chromosome(self.mutate_chromosome(y))

            self.resulting_population.append(individual)

        self.offspring_list = []

    # Selection to new population functions

    def create_new_population(self):
        """ Roulette wheel selection. """
        fitness_list = list()

        for individual in self.resulting_population:
            x = individual[0].get_float_representation()
            y = individual[1].get_float_representation()
            fitness = self.fitness_function(x, y)
            fitness_list.append(fitness)

        general_fitness = sum(fitness_list)
        # TODO: Check "roulette wheel" selection mechanism for correctness
        probabilities = list(map(lambda w: general_fitness / (w + 0.01), fitness_list))
        new_population = choices(self.resulting_population,
                                 weights=probabilities,
                                 k=self.POPULATION_SIZE)
        self.resulting_population = new_population
