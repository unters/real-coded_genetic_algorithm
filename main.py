from GeneticAlgorithm import GeneticAlgorithm
from functions import RosenbrockFunction
from functions import HimmelblauFunction
from functions import SphereFunction


def main():
    # sf = SphereFunction()
    # function = sf.function

    # rf = RosenbrockFunction()
    # function = rf.function

    hf = HimmelblauFunction()
    function = hf.function

    # sf.draw_plot()
    # rf.draw_plot()
    # hf.draw_plot()

    ga = GeneticAlgorithm(function)
    for i in range(ga.POPULATION_SIZE):
        print(ga.starting_population[i][0],
              ga.starting_population[i][1], "\t",
              ga.resulting_population[i][0],
              ga.resulting_population[i][1], end='\n')


if __name__ == "__main__":
    main()
