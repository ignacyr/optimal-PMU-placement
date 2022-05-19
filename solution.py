import numpy as np
import networkx as nx

from genetic_algorithm import genetic_alg


class OptimalSolution:
    def __init__(self, grid: nx.Graph, root, ga_params, figure):
        self.figure = figure
        self.root = root
        self.grid = grid
        self.ga_params = ga_params
        if not grid:
            self.solution = []
        else:
            self.solution = self.__use_alg()

    def __use_alg(self):
        # Reshape solution of Genetic Algorithm.
        solution = genetic_alg(self.grid, self.root, self.ga_params, self.figure).T
        solution = np.reshape(solution, (solution.size,))
        return solution
