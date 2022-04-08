import networkx as nx
import numpy as np
from optimal_pmu_placement import *
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(6, 7)
G.add_edge(7, 8)
G.add_edge(8, 9)
G.add_edge(3, 9)
G.add_edge(1, 5)
G.add_edge(1, 4)
G.add_edge(3, 7)
G.add_edge(5, 8)





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

