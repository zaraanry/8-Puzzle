
import random
import math

from copy import deepcopy
from chromosome import Chromosome

class GeneticsSolver:
    def __init__(self, puzzle, initial_population=1000, mutation_chance=0.9, cross_over_rate=0.3):
        self.puzzle = puzzle

        # parameters
        self.initial_population = initial_population
        self.mutation_chance = mutation_chance
        self.cross_over_rate = cross_over_rate

        # variables
        self.population = []
        self.best = None
        self.error = None

























#!/usr/bin/env python

from game import Pad
from solver import GeneticsSolver

MUTATION_CHANCE = 0.9
CROSS_OVER_RATE = 0.3
POPULATION_LEN = 1000
MAX_ITERATION = 1000


if __name__ == "__main__":
    try:
        p = Pad()
        p.shuffle()

        gSolver = GeneticsSolver(p, POPULATION_LEN, MUTATION_CHANCE, CROSS_OVER_RATE)
        gSolver.solve(max_iter=MAX_ITERATION)

        print('\n\n====================================================')
        print('Original:')
        print(p)
        print('Found Solution:')
        print(gSolver.best.gene)
        p.apply_chain(gSolver.best.gene, with_display=True)
        print('Result:')
        print(p)
    except KeyboardInterrupt:
        pass