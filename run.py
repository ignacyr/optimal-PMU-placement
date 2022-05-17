import networkx as nx
import numpy as np

import genetic_algorithm as ga
import plots
import random_grid_generator as rgg


def use_alg(r_grid):
    # Convert graph to adjacency matrix and fill diagonal with 1's.
    adjacency_matrix = nx.to_numpy_array(r_grid)
    np.fill_diagonal(adjacency_matrix, 1)

    # Reshape solution of Genetic Algorithm.
    ga_solution = ga.genetic_algorithm(adjacency_matrix).T
    ga_solution = np.reshape(ga_solution, (ga_solution.size,))
    return ga_solution


def main():
    min_buses, max_buses = 20, 30
    random_grid = rgg.RandomPowerGrid(min_buses, max_buses)

    ga_sol = use_alg(random_grid)

    print("Number of buses: ", random_grid.number_of_nodes())
    print("Genetic alg: ", ga_sol)
    print(len(ga_sol))

    # Bokeh
    plots.solution_plot(random_grid.number_of_nodes(), random_grid, ga_sol)


if __name__ == '__main__':
    main()
