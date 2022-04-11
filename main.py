import networkx as nx
import numpy as np
from optimal_pmu_placement import *
import matplotlib.pyplot as plt
import random as rd


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




print(edges)
print(G.nodes)
G.add_edges_from(edges)






# nx.draw(G, with_labels=True)
# plt.show()

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


# plt.figure()

nx.draw(G, node_color=color_map, with_labels=True)
plt.show()

