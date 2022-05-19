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

    def foo(placement, adjacency_m):  # dodać do warunku wykluczanie węzłów z jednym połączeniem
        number_of_pmu = placement.size
        for a in range(adjacency_m[0].size):
            bus_connections = np.add(adjacency_m[a].nonzero(), 1)
            if not np.any(np.intersect1d(placement, bus_connections)):  # observability
                return -1
        return number_of_pmu

    def fitness(placement, adjacency_m):
        number_of_pmu = foo(placement, adjacency_m)
        if number_of_pmu < 0:
            return -1
        points = 0
        for pmu in placement:
            points = points + 1 / np.sum(adjacency_m[pmu - 1])
        return points

    final_solution = np.array([0])
    number_of_buses = adjacency_matrix[0].size
    solutions = []
    rng = default_rng()
    solutions_number = ga_params['population_size']
    while not solutions:
        for i in range(solutions_number):
            n_of_pmu = rng.choice(number_of_buses) + 1
            solutions.append(rng.choice(number_of_buses, n_of_pmu, replace=False) + 1)

    best_solutions = []
    for i in range(ga_params['max_iter']):  # max number of iterations of genetic algorithm (generations)
        ranked_solutions = []
        for s in solutions:
            ranked_solutions.append((fitness(s, adjacency_matrix), s))
        ranked_solutions.sort(key=lambda y: y[0])
        ranked_solutions = list(filter(lambda x: x[0] > 0, ranked_solutions))

        if ranked_solutions:
            if 0 < fitness(ranked_solutions[0][1], adjacency_matrix) < fitness(final_solution, adjacency_matrix):
                final_solution = ranked_solutions[0][1]
            if not final_solution.any():
                final_solution = ranked_solutions[0][1]
            best_solutions = ranked_solutions[:solutions_number // 10]

        figure.update(grid, final_solution)  # Updating graph
        # print(final_solution)

        # print(f"=== Gen {i + 1} best solution === ")
        # print(final_score, final_solution)

        # For GUI
        iteration_of_alg = i + 1
        var.set(f"Iteration: {iteration_of_alg} / {ga_params['max_iter']}")
        root.update_idletasks()
        # For GUI

        elements = np.array([], dtype=int)
        num_of_els = np.array([], dtype=int)
        for s in best_solutions:
            elements = np.append(elements, s[1])
            num_of_els = np.append(num_of_els, s[1].size)
            elements = np.append(elements, rng.integers(number_of_buses) + 1)  # random bus as a mutation
        # have to add better mutations
        new_gen = []
        while len(new_gen) < solutions_number:
            size = np.min(num_of_els) - rng.integers(2)
            element = rng.choice(elements, size, replace=True)  # replace change to False!!!!!!!!!!!!
            element = np.unique(element.astype(int))
            new_gen.append(element)

        solutions = new_gen
    label.destroy()
    return final_solution
