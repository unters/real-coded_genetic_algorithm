from random import seed
from random import randint
from random import random
from random import uniform


class GeneticAlgorithm:
    """ Real-coded genetic algorithm:
    - chromosome - a real number as it is,
    - fixed population size,
    - elite selection,
    - flat crossover,
    - simple random mutation. """

    POPULATION_SIZE = 50
    POPULATIONS_LIMIT = 200
    CHROMOSOME_MUTATION_PROBABILITY = 0.2
    CHROMOSOME_MUTATION_BORDER = 0.2
    RANDOM_SEED = 1990

    # Keep starting population to compare with the resulting population
    starting_population = list()
    resulting_population = list()

    # Before adding offspring to resulting population we will save it to a
    # separate list to perform mutation
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

    # Population initialization functions

    def create_individual(self):
        """ Each individual consists of two chromosomes,
        each chromosome is represented by a float variable. """
        x = uniform(-4.0, 4.0)
        y = uniform(-4.0, 4.0)
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
        """ Two individuals flat crossover. In contrast to crossover operator
        used in canonical GA, in this real-coded crossover only one child is
        being formed. """
        first_parent_x = breeding_pair[0][0]
        first_parent_y = breeding_pair[0][1]
        second_parent_x = breeding_pair[1][0]
        second_parent_y = breeding_pair[1][1]

        max_x = max(first_parent_x, second_parent_x)
        min_x = min(first_parent_x, second_parent_x)
        max_y = max(first_parent_y, second_parent_y)
        min_y = min(first_parent_y, second_parent_y)

        child_x = uniform(min_x, max_x)
        child_y = uniform(min_y, max_y)

        child = [child_x, child_y]
        return child

    def population_crossover(self):
        """ Perform crossover for all selected individuals. """
        for i in range(self.POPULATION_SIZE):
            breeding_pair = self.panmixia_selection()

            if breeding_pair[0] != breeding_pair[1]:
                child = self.single_point_crossover(breeding_pair)
                self.offspring_list.append(child)

    # Mutation functions

    def mutate_chromosome(self, chromosome):
        """ Simple random mutation. A random value from segment
        (c - b; c + b) is assigned to chromosome, where c = value of
        chromosome before mutation, b = CHROMOSOME_MUTATION_BORDER. """
        c_min = chromosome - self.CHROMOSOME_MUTATION_BORDER
        c_max = chromosome + self.CHROMOSOME_MUTATION_BORDER
        mutated_chromosome = uniform(c_min, c_max)
        return mutated_chromosome

    def mutate_population(self):
        for individual in self.offspring_list:
            if random() < self.CHROMOSOME_MUTATION_PROBABILITY:
                x = individual[0]
                individual[0] = self.mutate_chromosome(x)

            if random() < self.CHROMOSOME_MUTATION_PROBABILITY:
                y = individual[1]
                individual[0] = self.mutate_chromosome(y)

            self.resulting_population.append(individual)

        self.offspring_list = []

    # Selection to new population functions

    def create_new_population(self):
        """ Elite selection. """
        fitness_list = list()

        for individual in self.resulting_population:
            x = individual[0]
            y = individual[1]
            fitness = self.fitness_function(x, y)
            fitness_list.append(fitness)

        new_population = sorted(list(zip(fitness_list, self.resulting_population)),
                                key=lambda f: f[0])

        self.resulting_population = []
        for i in range(self.POPULATION_SIZE):
            self.resulting_population.append(new_population[i][1])
