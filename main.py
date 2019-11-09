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