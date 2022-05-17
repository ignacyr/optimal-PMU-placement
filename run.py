import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import genetic_algorithm as ga
import numpy as np

import plots

# rd.seed(1234)

G = nx.Graph()
min_equal_max = 40  # minimum 3
n_of_buses_range = {'min': min_equal_max, 'max': min_equal_max}  # minimum 3
number_of_buses = int(rd.random()*(n_of_buses_range['max']+1 - n_of_buses_range['min'])) + n_of_buses_range['min']

# generate one random connection for every bus
connections = []
for i in range(1, number_of_buses+1):
    while len(connections) <= i:
        k = rd.randrange(1, number_of_buses)
        if i != k:
            connections.append((i, k))

# generate additional_conns % more random connections
additional_conns = 30  # [%]
for i in range(int(number_of_buses * additional_conns / 100)):
    while len(connections) <= number_of_buses + i:
        k = rd.randrange(1, number_of_buses)
        m = rd.randrange(1, number_of_buses)
        if m != k:
            connections.append((m, k))

# add connections to a graph
G.add_edges_from(connections)

# convert graph to adjacency matrix and fill diagonal with 1's
adjacency_matrix = nx.to_numpy_array(G)
np.fill_diagonal(adjacency_matrix, 1)

# reshape solution of Genetic Algorithm
GA_solution = ga.genetic_algorithm(adjacency_matrix).T
GA_solution = np.reshape(GA_solution, (GA_solution.size, ))

# color buses with PMU and draw graph
color_map = np.full(G.number_of_nodes(), 'magenta')
color_map[GA_solution-1] = 'yellow'
# nx.draw(G, node_color=color_map, with_labels=True)
# plt.show()

print("Number of buses: ", number_of_buses)
print("Genetic alg: ", GA_solution)
print(len(GA_solution))

GA_solution = []

# Bokeh
plots.solution_plot(number_of_buses, G, GA_solution)

