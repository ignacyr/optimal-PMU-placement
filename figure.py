import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Figure:
    def __init__(self, power_grid, root):
        self.power_grid = power_grid
        self.fig = plt.figure(figsize=(10, 6))
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.canvas = FigureCanvasTkAgg(self.fig, root)
        self.canvas.get_tk_widget().grid()

    def update(self, grid, solution):
        self.ax.clear()
        self.plot(grid, solution)
        self.canvas.draw()

    def plot(self, grid, solution):
        no_pmu = list(set(grid.nodes) - set(solution))
        pos = nx.spring_layout(grid, seed=1234)
        nx.draw_networkx_nodes(grid, nodelist=solution, node_color="green", pos=pos)
        nx.draw_networkx_nodes(grid, nodelist=no_pmu, node_color="red", pos=pos)
        # Drawing power grid model with electrical buses labels.
        nx.draw_networkx_edges(grid, pos=pos)
        # Drawing labels.
        labels_key_value = list(grid.nodes)
        labels = {labels_key_value[i]: labels_key_value[i] for i in range(len(labels_key_value))}
        nx.draw_networkx_labels(grid, labels=labels, pos=pos)

