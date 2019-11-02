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

    def _init_population(self):
        self.population = [Chromosome(puzzle=self.puzzle) for _ in range(self.initial_population)]

    def _calculate_error(self):
        if not self.population:
            return

        if self.best is None:
            self.best = self.population[0]

        error = 0
        for p in self.population:
            p.update_error()
            if p.error < self.best.error:
                self.best = deepcopy(p)
            error += p.error
        self.error = error / len(self.population)

    def _select_bests(self):
        totals = []
        running_total = 0

        for p in self.population:
            w = 1 / (0.000001 + p.error)
            running_total += w
            totals.append(running_total)

        def select_i():
            rnd = random.random() * running_total
            for i, total in enumerate(totals):
                if rnd < total:
                    return i

        result = []
        while len(result) < self.initial_population:
            i = select_i()
            result.append(self.population[i])
        self.population = result

    def _cross_over(self, always=False):
        if len(self.population) < 2:
            return

        cross_over_occur = math.ceil(len(self.population) * self.cross_over_rate)
        list_of_fertile_genes = [i for i in range(len(self.population))]

        for i in range(int(cross_over_occur)):
            a, b = random.sample(list_of_fertile_genes, 2)
            for idx, k in enumerate(list_of_fertile_genes):
                if k == b or k == a:
                    del list_of_fertile_genes[idx]

            offspring_a, offspring_b = Chromosome.cross_over(self.population[a], self.population[b])
            if (offspring_a.error < min(self.population[a].error, self.population[b].error) and \
               offspring_b.error < min(self.population[a].error, self.population[b].error)) or always:
                self.population[a] = offspring_a
                self.population[b] = offspring_b

    def _mutate(self):
        for i in self.population:
            if random.random() < self.mutation_chance:
                i.mutate(True)

    def solve(self, max_iter=1000, optimal_error=0):
        random.seed()
        self._init_population()

        iteration = 0
        while iteration < max_iter and (not self.best or self.best.error_puzzle_cost > optimal_error):
            self._cross_over(always=True)
            self._calculate_error()
            self._select_bests()
            self._mutate()

            self._display(iteration)
            iteration += 1

        return self.best

    def _display(self, iteration):
        print('~~~~~~~~ iteration: %d ~~~~~~~~' % iteration)
        print('population: len(%d)   Total Error(%0.4f)' % (
            len(self.population),
            self.error
        ))

        if self.best:
            print('best: %0.4f   ->   %0.4f  +  %0.4f' % (
                self.best.error,
                self.best.error_puzzle_cost,
                self.best.error_gene_len
            ))
            print('best is: %s' % self.best)
        # for p in self.population:
        #     p.update_fitness()
        #     print('    - %0.4f   ->   %0.4f  +  %0.4f' % (
        #         p.Fitness,
        #         p.Error,
        #         p.Regularization
        #     ))
        # sleep(01.1)
        print('--------------------------------')import random
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

    def _init_population(self):
        self.population = [Chromosome(puzzle=self.puzzle) for _ in range(self.initial_population)]

    def _calculate_error(self):
        if not self.population:
            return

        if self.best is None:
            self.best = self.population[0]

        error = 0
        for p in self.population:
            p.update_error()
            if p.error < self.best.error:
                self.best = deepcopy(p)
            error += p.error
        self.error = error / len(self.population)

    def _select_bests(self):
        totals = []
        running_total = 0

        for p in self.population:
            w = 1 / (0.000001 + p.error)
            running_total += w
            totals.append(running_total)

        def select_i():
            rnd = random.random() * running_total
            for i, total in enumerate(totals):
                if rnd < total:
                    return i

        result = []
        while len(result) < self.initial_population:
            i = select_i()
            result.append(self.population[i])
        self.population = result

    def _cross_over(self, always=False):
        if len(self.population) < 2:
            return

        cross_over_occur = math.ceil(len(self.population) * self.cross_over_rate)
        list_of_fertile_genes = [i for i in range(len(self.population))]

        for i in range(int(cross_over_occur)):
            a, b = random.sample(list_of_fertile_genes, 2)
            for idx, k in enumerate(list_of_fertile_genes):
                if k == b or k == a:
                    del list_of_fertile_genes[idx]

            offspring_a, offspring_b = Chromosome.cross_over(self.population[a], self.population[b])
            if (offspring_a.error < min(self.population[a].error, self.population[b].error) and \
               offspring_b.error < min(self.population[a].error, self.population[b].error)) or always:
                self.population[a] = offspring_a
                self.population[b] = offspring_b

    def _mutate(self):
        for i in self.population:
            if random.random() < self.mutation_chance:
                i.mutate(True)

    def solve(self, max_iter=1000, optimal_error=0):
        random.seed()
        self._init_population()

        iteration = 0
        while iteration < max_iter and (not self.best or self.best.error_puzzle_cost > optimal_error):
            self._cross_over(always=True)
            self._calculate_error()
            self._select_bests()
            self._mutate()

            self._display(iteration)
            iteration += 1

        return self.best

    def _display(self, iteration):
        print('~~~~~~~~ iteration: %d ~~~~~~~~' % iteration)
        print('population: len(%d)   Total Error(%0.4f)' % (
            len(self.population),
            self.error
        ))

        if self.best:
            print('best: %0.4f   ->   %0.4f  +  %0.4f' % (
                self.best.error,
                self.best.error_puzzle_cost,
                self.best.error_gene_len
            ))
            print('best is: %s' % self.best)
        # for p in self.population:
        #     p.update_fitness()
        #     print('    - %0.4f   ->   %0.4f  +  %0.4f' % (
        #         p.Fitness,
        #         p.Error,
        #         p.Regularization
        #     ))
        # sleep(01.1)
        print('--------------------------------')import random
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

    def _init_population(self):
        self.population = [Chromosome(puzzle=self.puzzle) for _ in range(self.initial_population)]

    def _calculate_error(self):
        if not self.population:
            return

        if self.best is None:
            self.best = self.population[0]

        error = 0
        for p in self.population:
            p.update_error()
            if p.error < self.best.error:
                self.best = deepcopy(p)
            error += p.error
        self.error = error / len(self.population)

    def _select_bests(self):
        totals = []
        running_total = 0

        for p in self.population:
            w = 1 / (0.000001 + p.error)
            running_total += w
            totals.append(running_total)

        def select_i():
            rnd = random.random() * running_total
            for i, total in enumerate(totals):
                if rnd < total:
                    return i

        result = []
        while len(result) < self.initial_population:
            i = select_i()
            result.append(self.population[i])
        self.population = result

    def _cross_over(self, always=False):
        if len(self.population) < 2:
            return

        cross_over_occur = math.ceil(len(self.population) * self.cross_over_rate)
        list_of_fertile_genes = [i for i in range(len(self.population))]

        for i in range(int(cross_over_occur)):
            a, b = random.sample(list_of_fertile_genes, 2)
            for idx, k in enumerate(list_of_fertile_genes):
                if k == b or k == a:
                    del list_of_fertile_genes[idx]

            offspring_a, offspring_b = Chromosome.cross_over(self.population[a], self.population[b])
            if (offspring_a.error < min(self.population[a].error, self.population[b].error) and \
               offspring_b.error < min(self.population[a].error, self.population[b].error)) or always:
                self.population[a] = offspring_a
                self.population[b] = offspring_b

    def _mutate(self):
        for i in self.population:
            if random.random() < self.mutation_chance:
                i.mutate(True)

    def solve(self, max_iter=1000, optimal_error=0):
        random.seed()
        self._init_population()

        iteration = 0
        while iteration < max_iter and (not self.best or self.best.error_puzzle_cost > optimal_error):
            self._cross_over(always=True)
            self._calculate_error()
            self._select_bests()
            self._mutate()

            self._display(iteration)
            iteration += 1

        return self.best

    def _display(self, iteration):
        print('~~~~~~~~ iteration: %d ~~~~~~~~' % iteration)
        print('population: len(%d)   Total Error(%0.4f)' % (
            len(self.population),
            self.error
        ))

        if self.best:
            print('best: %0.4f   ->   %0.4f  +  %0.4f' % (
                self.best.error,
                self.best.error_puzzle_cost,
                self.best.error_gene_len
            ))
            print('best is: %s' % self.best)
        # for p in self.population:
        #     p.update_fitness()
        #     print('    - %0.4f   ->   %0.4f  +  %0.4f' % (
        #         p.Fitness,
        #         p.Error,
        #         p.Regularization
        #     ))
        # sleep(01.1)
        print('--------------------------------')import numpy as np
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