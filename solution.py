import numpy as np
import networkx as nx

from genetic_algorithm import genetic_alg


class OptimalSolution:
    def __init__(self, grid: nx.Graph):
        self.grid = grid
        if not grid:
            self.solution = []
        else:
            self.solution = self.__use_alg()

    def __use_alg(self):
        # Convert graph to adjacency matrix and fill diagonal with 1's.
        adjacency_matrix = nx.to_numpy_array(self.grid)
        np.fill_diagonal(adjacency_matrix, 1)

        # Reshape solution of Genetic Algorithm.
        solution = genetic_alg(adjacency_matrix).T
        solution = np.reshape(solution, (solution.size,))
        return solution
