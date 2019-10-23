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























import numpy as np
from random import randint, choice

class Pad:
    def __init__(self):
        self.board = np.zeros((3, 3))

        index = 0
        for i in range (3):
            for j in range (3):
                self.board[i, j] = index
                index += 1

    def swap(self, a, b):
        temp = self.board[a]
        self.board[a] = self.board[b]
        self.board[b] = temp

    def move_left(self):
        index = np.where(self.board == 0)
        if index[1] == 2:
            return False
        move_to = (index[0], index[1]+1)
        self.swap(index, move_to)
        return True

    def move_right(self):
        index = np.where(self.board == 0)
        if index[1] == 0:
            return False
        move_to = (index[0], index[1]-1)
        self.swap(index, move_to)
        return True

    def move_up(self):
        index = np.where(self.board == 0)
        if index[0] == 2:
            return False
        move_to = (index[0]+1, index[1])
        self.swap(index, move_to)
        return True

    def move_down(self):
        index = np.where(self.board == 0)
        if index[0] == 0:
            return False
        move_to = (index[0]-1, index[1])
        self.swap(index, move_to)
        return True

    def __str__(self):
        result = ''
        for i in range(3):
            result += '| '
            for j in range(3):
                result += '%s | ' % (str(int(self.board[i, j])) if self.board[i, j] != 0 else ' ')
            result += '\n'
        return result
    
    def shuffle(self):
        for i in range(randint(10, 100)):
            f = choice([
                self.move_down,
                self.move_up,
                self.move_right,
                self.move_left
            ])
            f()

    def apply_chain(self, chain, with_display=False):
        chain_map = {
            'up': self.move_up,
            'down': self.move_down,
            'left': self.move_left,
            'right': self.move_right,
        }
        for ch in chain:
            chain_map[ch]()
            if with_display:
                print(self)

    def cost(self):
        reference = {
            0: (0, 0),
            1: (0, 1),
            2: (0, 2),

            3: (1, 0),
            4: (1, 1),
            5: (1, 2),

            6: (2, 0),
            7: (2, 1),
            8: (2, 2),
        }

        error = 0.0
        for i in range(9):
            index = np.where(self.board == i)
            ref_index = reference[i]
            error += (index[0] - ref_index[0]) ** 2 + (index[1] - ref_index[1]) ** 2
        error /= 9.0
        return error[0]