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
        return '(%d)  %s' % (len(self.gene), ' -> '.join(self.gene))