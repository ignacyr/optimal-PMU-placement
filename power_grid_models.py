import random as rd

import networkx as nx


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


class UserDefinedGrid(nx.Graph):
    def __init__(self, nodes_number_entry, incoming_graph_data=None, **attr):
        super().__init__(incoming_graph_data, **attr)
        self.add_nodes_from(list(range(1, nodes_number_entry+1)))
