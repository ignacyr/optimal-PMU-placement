import networkx as nx
import numpy as np
from optimal_pmu_placement import *
import matplotlib.pyplot as plt
import random as rd
from genetic_algorithm import genetic_algorithm


G = nx.Graph()
number_of_nodes = int(rd.random()*20)+20
G.add_nodes_from(np.linspace(1, number_of_nodes, number_of_nodes, dtype='int'))
edges = []
for i in range(1, number_of_nodes+1):
    zmienna_pomocnicza = True
    while zmienna_pomocnicza:
        j = rd.randrange(1, number_of_nodes)
        if i != j:
            edges.append((i, j))
            zmienna_pomocnicza = False
for k in range(10):
    j = rd.randrange(1, number_of_nodes)
    i = rd.randrange(1, number_of_nodes)
    if i != j:
        edges.append((i, j))

G.add_edges_from(edges)

bla = nx.to_numpy_array(G)

np.fill_diagonal(bla, 1)

B = bla

# A = np.array([[0., 1., 1., 0., 1., 1.],
#               [1., 0., 0., 1., 0., 0.],
#               [1., 0., 0., 1., 0., 0.],
#               [0., 1., 1., 0., 0., 0.],
#               [1., 0., 0., 0., 0., 0.],
#               [1., 0., 0., 0., 0., 0.]])
#
# np.fill_diagonal(A, 1)

wynik_dfs = dfs(B).T
wynik_dfs = np.reshape(wynik_dfs, (wynik_dfs.size, ))
print(wynik_dfs)
color_map = np.full(G.number_of_nodes(), 'magenta')
color_map[wynik_dfs-1] = 'yellow'

# nx.draw(G, node_color=color_map, with_labels=True)
# plt.show()

wynik_gen = np.array(genetic_algorithm(B)).T
wynik_gen = np.reshape(wynik_gen, (wynik_gen.size, ))
print(wynik_gen)
color_map = np.full(G.number_of_nodes(), 'magenta')
color_map[wynik_gen-1] = 'yellow'

nx.draw(G, node_color=color_map, with_labels=True)
plt.show()

print("DFS:         ", wynik_dfs)
print("Genetic alg: ", wynik_gen)
