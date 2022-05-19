import networkx as nx
import numpy as np
import random as rd
import matplotlib.pyplot as plt

from genetic_algorithm import genetic_alg


class OptimalSolution:
    def __init__(self, grid: nx.Graph):
        self.grid = grid
        self.solution = self.__use_alg()

    def __use_alg(self):
        # Convert graph to adjacency matrix and fill diagonal with 1's.
        adjacency_matrix = nx.to_numpy_array(self.grid)
        np.fill_diagonal(adjacency_matrix, 1)

        # Reshape solution of Genetic Algorithm.
        solution = genetic_alg(adjacency_matrix).T
        solution = np.reshape(solution, (solution.size,))
        return solution


class RandomGrid(nx.Graph):
    """
    Class based on networkx.Graph class.
    It initializes base object and generates random nodes and edges
    for given min and max number of electrical buses.
    It is a simple model of a power system.
    """
    def __init__(self, min_buses, max_buses, incoming_graph_data=None, **attr):
        """Initialize base object and generate random nodes and edges."""
        super().__init__(incoming_graph_data, **attr)

        number_of_buses = int(rd.random() * (max_buses - min_buses)) + min_buses

        # Generate one random connection for every bus
        connections = []
        for i in range(1, number_of_buses + 1):
            while len(connections) <= i:
                k = rd.randrange(1, number_of_buses)
                if i != k:
                    connections.append((i, k))

        # Generate additional_conns % more random connections
        additional_conns = 30  # [%]
        for i in range(int(number_of_buses * additional_conns / 100)):
            while len(connections) <= number_of_buses + i:
                k = rd.randrange(1, number_of_buses)
                m = rd.randrange(1, number_of_buses)
                if m != k:
                    connections.append((m, k))

        self.add_edges_from(connections)


class Figure:
    def __init__(self, canvas, grid):
        self.grid = grid
        self.fig = plt.figure(0)
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.canvas = canvas

    def update(self, solution):
        self.ax.clear()
        self.plot(solution)
        self.canvas.draw()

    def plot(self, solution):
        no_pmu = list(set(self.grid.nodes) - set(solution))
        pos = nx.spring_layout(self.grid, seed=1234)
        nx.draw_networkx_nodes(self.grid, nodelist=solution, node_color="green", pos=pos)
        nx.draw_networkx_nodes(self.grid, nodelist=no_pmu, node_color="red", pos=pos)

        # Drawing power grid model with electrical buses labels.
        nx.draw_networkx_edges(self.grid, pos=pos)

        # Drawing labels.
        labels_key_value = list(self.grid.nodes)
        labels = {labels_key_value[i]: labels_key_value[i] for i in range(len(labels_key_value))}
        nx.draw_networkx_labels(self.grid, labels=labels, pos=pos)

