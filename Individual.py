import numpy as np
import random


class Individual:
    # initialize
    def __init__(self,
                 nqueens=8,
                 mutate_rate=0.1
                 ):
        self.nq = nqueens
        self.chromosome = list(np.arange(self.nq))
        self.fitness = 0
        np.random.shuffle(self.chromosome)  # Randomly generate a chromosome
        self.update_fitness()  # Calculate the fitness of each individual chromosome
        self.mr = mutate_rate

    def update_fitness(self):
        """
        number of non-attacking pairs of queens
        min = 0, max = 8 × 7/2 = 28
        In 8 Queens setting
        returns 28 - <A solution found>
        Calculate the fitness of each individual chromosome
        """
        value = 0
        for i in range(len(self.chromosome)):
            for j in range(i + 1, len(self.chromosome)):
                if self.chromosome[i] != self.chromosome[j]:  # case not in the same row
                    x = j - i
                    y = abs(self.chromosome[i] - self.chromosome[j])
                    if x != y:  # case non-attacking each other diagonally
                        value += 1
        self.fitness = value

    def mutate(self):
        """
        - according to genetic theory, a mutation will take place
        when there is an anomaly during cross over state
        - since a computer cannot determine such anomaly, we can define
        the probability of developing such a mutation
        """
        mutate_random = random.random()
        if mutate_random < self.mr:
            c = np.random.randint(8)
            self.chromosome[c] = np.random.randint(8)
            self.update_fitness()
            # print("Mutation happening!")
