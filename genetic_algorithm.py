import numpy as np
from numpy.random import default_rng
import tkinter as tk
import networkx as nx


def genetic_alg(grid, root, ga_params, figure):
    # Convert graph to adjacency matrix and fill diagonal with 1's.
    adjacency_matrix = nx.to_numpy_array(grid)
    np.fill_diagonal(adjacency_matrix, 1)

    # For GUI
    iteration_of_alg = 0
    var = tk.StringVar()
    var.set(f"{iteration_of_alg} / {ga_params['max_iter']}")
    label = tk.Label(root, textvariable=var)
    label.grid()
    # For GUI

    if len(adjacency_matrix) == 0:
        return []

    def target(placement, adjacency_m):  # dodać do warunku wykluczanie węzłów z jednym połączeniem
        number_of_pmu = placement.size
        for a in range(adjacency_m[0].size):
            bus_connections = np.add(adjacency_m[a].nonzero(), 1)
            if not np.any(np.intersect1d(placement, bus_connections)):  # observability
                return -1
        return number_of_pmu

    def fitness(placement, adjacency_m):
        number_of_pmu = target(placement, adjacency_m)
        if number_of_pmu < 0:
            return -1
        points = 0
        for pmu in placement:
            points = points + 1 / np.sum(adjacency_m[pmu - 1])
        return points

    def selection(population, final_sol):
        best_sols = []
        ranked_sols = []
        for p in population:
            ranked_sols.append((fitness(p, adjacency_matrix), p))
        ranked_sols.sort(key=lambda y: y[0])
        ranked_sols = list(filter(lambda x: x[0] > 0, ranked_sols))
        if ranked_sols:
            if 0 < fitness(ranked_sols[0][1], adjacency_matrix) < fitness(final_sol, adjacency_matrix):
                final_sol = ranked_sols[0][1]
            if not final_solution.any():
                final_sol = ranked_sols[0][1]
            best_sols = ranked_sols[:solutions_number // 10]
        return best_sols, final_sol

    def crossover(best_sols):
        best_elements = np.array([], dtype=int)
        num_of_els = np.array([], dtype=int)
        for bs in best_sols:
            best_elements = np.append(best_elements, bs[1])
            num_of_els = np.append(num_of_els, bs[1].size)
            best_elements = np.append(best_elements, rng.integers(number_of_buses) + 1)  # random bus as a mutation
        # have to add better mutations
        new_gen = []
        while len(new_gen) < solutions_number:
            size = np.min(num_of_els) - rng.integers(2)
            element = rng.choice(best_elements, size, replace=True)  # replace change to False!!!!!!!!!!!!
            element = np.unique(element.astype(int))
            new_gen.append(element)
        return new_gen

    def mutation():
        pass

    final_solution = np.array([0])
    number_of_buses = adjacency_matrix[0].size
    all_solutions = []
    rng = default_rng()
    solutions_number = ga_params['population_size']
    while not all_solutions:
        for i in range(solutions_number):
            n_of_pmu = rng.choice(number_of_buses) + 1
            all_solutions.append(rng.choice(number_of_buses, n_of_pmu, replace=False) + 1)

    best_solutions = []
    for i in range(ga_params['max_iter']):  # max number of iterations of genetic algorithm (generations)
        best_solutions = selection(all_solutions, final_solution)
        all_solutions = crossover(best_solutions)
        mutation()


        # For GUI
        figure.update(grid, final_solution)
        iteration_of_alg = i + 1
        var.set(f"Iteration: {iteration_of_alg} / {ga_params['max_iter']}")
        root.update_idletasks()
        # For GUI

        solutions = crossover(best_solutions)

    label.destroy()

    return final_solution
