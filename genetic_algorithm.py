import numpy as np
from numpy.random import default_rng
import networkx as nx
import math


def foo(placement, adjacency_m):
    number_of_pmu = placement.size
    for i in range(adjacency_m[0].size):
        bus_connections = np.add(adjacency_m[i].nonzero(), 1)
        if not np.any(np.intersect1d(placement, bus_connections)):  # observability
            return -1
    return number_of_pmu


def fitness(placement, adjacency_m):
    ans = foo(placement, adjacency_m)
    return ans


def genetic_algorithm(adjacency_matrix):
    final_solution = 0
    number_of_buses = adjacency_matrix[0].size
    solutions = []
    rng = default_rng()
    for i in range(10000):
        n_of_pmu = rng.choice(number_of_buses) + 1
        solutions.append(rng.choice(number_of_buses, n_of_pmu, replace=False) + 1)

    for i in range(50):  # max number of iterations of genetic algorithm
        ranked_solutions = []
        for s in solutions:
            ranked_solutions.append((fitness(s, adjacency_matrix), s))
        ranked_solutions.sort(key=lambda y: y[0])
        ranked_solutions = list(filter(lambda x: x[0] > 0, ranked_solutions))

        print(f"=== Gen {i} best solution === ")
        if ranked_solutions:
            print(ranked_solutions[0])
            final_solution = ranked_solutions[0][1]
            best_solutions = ranked_solutions[:10]
        else:
            return final_solution

        elements = np.array([], dtype=int)
        num_of_els = np.array([], dtype=int)
        for s in best_solutions:
            elements = np.append(elements, s[1])
            num_of_els = np.append(num_of_els, s[1].size)
            elements = np.append(elements, rng.integers(number_of_buses)+1)
        new_gen = []
        for _ in range(2000):
            size = np.min(num_of_els) + rng.integers(5) - 2
            element = rng.choice(elements, size, replace=True)
            new_gen.append(np.unique(element.astype(int)))
        solutions = new_gen
    return final_solution
