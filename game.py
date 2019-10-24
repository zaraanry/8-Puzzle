import random
from copy import deepcopy

class Chromosome:
    VALID_MOVES = ['up', 'down', 'left', 'right']

    def __init__(self, puzzle, gene=None):
        if gene is None:
            gene = []

        self.error = None
        self.error_puzzle_cost = None
        self.error_gene_len = None
        self.puzzle = puzzle
        self.gene = gene
        self.update_error()

    def update_error(self):
        temp = deepcopy(self.puzzle)
        temp.apply_chain(self.gene)

        self.error_puzzle_cost = temp.cost()
        self.error_gene_len = len(self.gene) * 0.01
        self.error = self.error_puzzle_cost + self.error_gene_len

    @staticmethod
    def cross_over(a, b):
        if len(b.gene) > len(a.gene):
            return Chromosome.cross_over(b, a)

        geneA = []
        geneB = []

        len_a = len(a.gene)
        len_b = len(b.gene)

        for i in range(len_b):
            if random.random() < 0.5:
                geneA.append(a.gene[i])
                geneB.append(b.gene[i])
            else:
                geneA.append(b.gene[i])
                geneB.append(a.gene[i])

        if len_b != len_a:
            for i in range(len_a-len_b):
                geneA.append(a.gene[len_b+i])

        return Chromosome(a.puzzle, geneA), Chromosome(b.puzzle, geneB)

    def mutate(self, allow_only_growing=False):
        add_vs_mutate_chance = 0.5
        if not self.gene:
            add_vs_mutate_chance = 1.0

        if random.random() < add_vs_mutate_chance:
            self.gene.append(random.choice(self.VALID_MOVES))
        else:
            i = random.randint(0, len(self.gene)-1)
            self.gene[i] = random.choice(self.VALID_MOVES)

    def __str__(self):
        return '(%d)  %s' % (len(self.gene), ' -> '.join(self.gene))import numpy as np
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