import numpy as np
import random
import sys

from Individual import Individual


class Game:
    population: list[Individual]

    # initialize
    def __init__(self,
                 population_size=100,
                 mutate_flag=True,
                 goal_control=28
                 ):
        self.p_size = population_size
        self.population = [Individual() for i in range(population_size)]
        self.mutateflag = mutate_flag
        self.goal_ctl = goal_control
        # summation_fitness = np.sum([x.fitness for x in self.population])
        # for each in self.population:
        #     each.survival = each.fitness / (summation_fitness * 1.0)

    def select_parent(self):
        """
        return the chosen index i
        Parent chromosomes are selected with a probability related to their fitness.
        Algorithm: roulette weighted by fitness
        Reproduction rate(i) = fitness(i) / sum(fitniess(k))
        """
        # calculate the sum of all individuals' fitness
        total_score = 0
        for each in self.population:
            total_score += each.fitness

        # roulette weighted by fitness
        num = random.randint(0, total_score)
        current_score = 0
        for i in range(len(self.population)):
            current_score += self.population[i].fitness
            if current_score >= num:
                return i

    def crossover(self, parent1, parent2):
        n = len(parent1.chromosome)
        c = random.randint(0, n)
        child = Individual()
        child.chromosome = []
        child.chromosome.extend(parent1.chromosome[0:c])
        child.chromosome.extend(parent2.chromosome[c:])
        child.update_fitness()
        return child

    def genetic_algorithm(self):
        new_population: list[Individual] = []
        for i in range(len(self.population)):
            parent1 = self.population[self.select_parent()]
            parent2 = self.population[self.select_parent()]
            # print("Parents generated : ", parent1, parent2)
            child = self.crossover(parent1, parent2)
            if self.mutateflag:
                child.mutate()
            new_population.append(child)
        self.population = new_population

    def goal_test(self):
        goals = []
        for each in self.population:
            if each.fitness == self.goal_ctl and each.chromosome not in goals:
                goals.append(each.chromosome)
        return goals

    def assess(self):
        total_score = 0
        for each in self.population:
            total_score += each.fitness
        return total_score / len(self.population)