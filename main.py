from Game import Game
from Individual import Individual


def main():
    # indvd1 = Individual()
    # indvd2 = Individual()
    # # indvd.chromosome = [3,5,6,0,7,7,6,3]
    # indvd1.chromosome = [3, 5, 7, 4, 6, 0, 2, 4]
    # indvd2.chromosome = [3, 5, 7, 1, 6, 0, 5, 4]
    # indvd1.update_fitness()
    # indvd2.update_fitness()
    # print(indvd1.fitness)
    # print(indvd2.fitness)

    g = Game(100)
    iteration_limit = 5000000  # iteration limit

    print("POPULATION size : ", g.p_size)
    iteration = 1
    solutions = []
    while True:
        print("#" * 5, "Executing Generation : ", iteration, "#" * 5, "Found Solutions", len(solutions), "Population "
                                                                                                         "assessment "
                                                                                                         "is:",
              round(g.assess(), 2))
        subsltn = g.goal_test()
        if len(subsltn) > 0:
            for each1 in subsltn:
                if each1 not in solutions:
                    print("#" * 5, "Find the ", len(solutions) + 1, "th solution in Genetic generation : ", iteration,
                          "#" * 5)
                    print(each1)
                    solutions.append(each1)
        if iteration >= iteration_limit or len(solutions) == 92:
            break
        # keep iterating till finding the best chromosome
        g.genetic_algorithm()
        iteration += 1

    nsltn = len(solutions)
    print("#" * 10, "All", nsltn, "SOLUTIONS : ", "#" * 10)
    if nsltn > 0:
        for x in solutions:
            print(x)
    else:
        print("no solutions")


if __name__ == "__main__":
    main()

'''
Core Working:

Initialization : The initialization contains of the randomly distributed population that is generated. Lower 
population size will lead to lots of time in computation of approximate solution. And higher value will cause 
internal iterations to increase. Therefore choose population size carefully. In this example we have tried with 
population size of 100 , 500 and 1000 

Selection of parents: Just as evolutionary biology requires two parents to undergo meiosis, so does GA. Therefore 
there is need to select two parents which determine a child. The calculation in determining the parents is elaborated 
later 

CrossOver / Reproduction : Once parents having high fitness are selected, crossover essentially marks the recombining 
of genetic materials / chromosomes to produce a healthy offspring 

Mutation : Mutation may or may not occur. In case mutation occurs, it forces a random value of child to change , 
thereby shifting the algorithm in either a positive or negative route 

Generation of new population : For all population, a child must be computed. Therefore, the new population can be 
said to be a list dynamically populated by the children computed. 

Assessment: the measure of fitness of any individual (chessboard arrangement) is attributed to number of clashes 
amongst attacking positions of queens. 
'''
