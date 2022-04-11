import numpy as np
from numpy.random import default_rng
import networkx as nx
import math


def foo(placement, adjacency_m):
    number_of_pmu = placement.size
    for i in range(adjacency_m[:, 0].size):
        bus_connections = np.add(adjacency_m[i].nonzero(), 1)
        if not np.any(np.intersect1d(placement, bus_connections)):  # observability
            return -1
    return number_of_pmu


def fitness(placement, adjacency_m):
    ans = foo(placement, adjacency_m)
    return ans


def genetic_algorithm(A):
    answer = 0
    number_of_buses = A[0].size
    solutions = []
    for i in range(10000):
        rng = default_rng()
        n_of_pmu = rng.choice(number_of_buses) + 1
        solutions.append(rng.choice(number_of_buses, n_of_pmu, replace=False) + 1)

    for i in range(50):  # max number of iterations of genetic algorithm
        rankedSolutions = []
        for s in solutions:
            rankedSolutions.append((fitness(s, A), s))
        rankedSolutions.sort(key=lambda y: y[0])
        rankedSolutions = list(filter(lambda x: x[0] > 0, rankedSolutions))

        print(f"=== Gen {i} best solution === ")
        print(rankedSolutions[0])
        answer = rankedSolutions[0][1]
        bestSolutions = rankedSolutions[:10]

        elements = np.array([], dtype=int)
        num_of_els = np.array([], dtype=int)
        for s in bestSolutions:
            elements = np.append(elements, s[1])
            num_of_els = np.append(num_of_els, s[1].size)

        newGen = []
        for _ in range(1000):
            rng = default_rng()
            size = rng.choice(num_of_els)
            element = np.round(rng.choice(elements, size, replace=False))  # * rng.uniform(0.99, 1.01, size)) mutacja nie działa
            newGen.append(element.astype(int))
        solutions = newGen
    return answer
