import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import genetic_algorithm as ga
import numpy as np

from bokeh.plotting import figure, show, from_networkx

# rd.seed(1234)

G = nx.Graph()
number_of_buses = int(rd.random()*10)+10  # generate random number of buses

# generate one random connection for every bus
connections = []
for i in range(1, number_of_buses+1):
    while len(connections) <= i:
        k = rd.randrange(1, number_of_buses)
        if i != k:
            connections.append((i, k))

# generate 10 more random connections
for i in range(10):
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

# reshape solution of DFS algorithm
# dfs_solution = dfs.dfs(adjacency_matrix).T
# dfs_solution = np.reshape(dfs_solution, (dfs_solution.size, ))

# reshape solution of Genetic Algorithm
GA_solution = ga.genetic_algorithm(adjacency_matrix).T
GA_solution = np.reshape(GA_solution, (GA_solution.size, ))

# color buses with PMU and draw graph
color_map = np.full(G.number_of_nodes(), 'magenta')
color_map[GA_solution-1] = 'yellow'
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()

print("Number of buses: ", number_of_buses)
print("Genetic alg: ", GA_solution)
print(len(GA_solution))

p = figure(title="Some graph", x_range=(-1.1, 1.1), y_range=(-1.1, 1.1), tools="", toolbar_location=None)

g = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
p.renderers.append(g)

show(p)


