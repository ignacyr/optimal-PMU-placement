import networkx as nx
import numpy as np
from optimal_pmu_placement import *
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([(4, {"abc": 123}), (5, {"abc": 0})])
G.add_edge(5, 2)
G.add_edge(1, 6)
G.add_edges_from([(6, 3),
                  (3, 4)])
G.add_edges_from([(1, 5),
                  (2, 4)])

# nx.draw(G, with_labels=True)
# plt.show()

bla = nx.to_numpy_array(G)

np.fill_diagonal(bla, 1)

B = bla

A = np.array([[0., 1., 1., 0., 1., 1.],
              [1., 0., 0., 1., 0., 0.],
              [1., 0., 0., 1., 0., 0.],
              [0., 1., 1., 0., 0., 0.],
              [1., 0., 0., 0., 0., 0.],
              [1., 0., 0., 0., 0., 0.]])

np.fill_diagonal(A, 1)

wynik_dfs = dfs(B).T
wynik_dfs = np.reshape(wynik_dfs, (wynik_dfs.size, ))
print(wynik_dfs)
color_map = np.full(G.size(), 'darkblue')
color_map[wynik_dfs-1] = 'magenta'


# plt.figure()
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()

