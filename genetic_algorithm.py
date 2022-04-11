import numpy as np
from numpy.random import default_rng
import networkx as nx


def foo(placement, adjacency_m):
    number_of_pmu = placement.size
    # buses = np.linspace(1, adjacency_m[:, 0].size, adjacency_m[:, 0].size)
    for i in range(adjacency_m[:, 0].size):
        bus_connections = np.add(adjacency_m[i].nonzero(), 1)
        if not np.any(np.intersect1d(placement, bus_connections)):  # observability
            return -1
    return number_of_pmu


def fitness(placement, adjacency_m):
    ans = foo(placement, adjacency_m)
    return ans


A = np.array([[1., 1., 1., 0., 1., 1.],
              [1., 1., 0., 1., 0., 0.],
              [1., 0., 1., 1., 0., 0.],
              [0., 1., 1., 1., 0., 0.],
              [1., 0., 0., 0., 1., 0.],
              [1., 0., 0., 0., 0., 1.]])


number_of_buses = 6
solutions = []
for i in range(1000):
    rng = default_rng()
    n_of_pmu = rng.choice(number_of_buses) + 1
    solutions.append(rng.choice(number_of_buses, n_of_pmu, replace=False) + 1)


# for i in range(10000):  # max number of iterations of genetic algorithm
rankedSolutions = []
for s in solutions:
    rankedSolutions.append((fitness(s, A), s))
rankedSolutions.sort(key=lambda y: y[0])
rankedSolutions = list(filter(lambda x: x[0] > 0, rankedSolutions))

    # print(f"=== Gen {i} best solution === ")
    # print(rankedSolutions[0])

bestSolutions = rankedSolutions[:100]

elements = np.array([], dtype=int)
num_of_els = np.array([], dtype=int)
for s in bestSolutions:
    elements = np.append(elements, s[1])
    num_of_els = np.append(num_of_els, s[1].size)

newGen = []
for _ in range(1000):
    rng = default_rng()
    size = rng.choice(num_of_els)
    element = rng.choice(elements, size, replace=False)
    newGen.append(element)


# # def fitness(adjacency_m):
# A = np.array([[1., 1., 1., 0., 1., 1.],
#               [1., 1., 0., 1., 0., 0.],
#               [1., 0., 1., 1., 0., 0.],
#               [0., 1., 1., 1., 0., 0.],
#               [1., 0., 0., 0., 1., 0.],
#               [1., 0., 0., 0., 0., 1.]])
#
# place = np.array([3, 2, 4])
# print(foo(place, A))
#
# X = A
# np.fill_diagonal(X, 0)
# G = nx.from_numpy_matrix(X)
# new_labels = dict(zip(np.linspace(0, A[:, 0].size-1, A[:, 0].size, dtype=int),
#                       np.linspace(1, A[:, 0].size, A[:, 0].size, dtype=int)))
# G = nx.relabel_nodes(G, new_labels)
# nx.draw(G, with_labels=True)
