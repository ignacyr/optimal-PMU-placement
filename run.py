import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

import genetic_algorithm as ga
import random_grid_generator as rgg

import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import ttk
# # # Implement the default Matplotlib key bindings.
# # from matplotlib.backend_bases import key_press_handler
# from matplotlib.figure import Figure


def use_alg(r_grid):
    # Convert graph to adjacency matrix and fill diagonal with 1's.
    adjacency_matrix = nx.to_numpy_array(r_grid)
    np.fill_diagonal(adjacency_matrix, 1)

    # Reshape solution of Genetic Algorithm.
    ga_solution = ga.genetic_algorithm(adjacency_matrix).T
    ga_solution = np.reshape(ga_solution, (ga_solution.size,))
    return ga_solution

def jaka():
    pass





def main():
    # Minimum and maximum number of electrical buses in a randomly generated power grid model.
    min_buses, max_buses = 40, 50

    # Generating a random power system model.
    random_grid = rgg.RandomPowerGrid(min_buses, max_buses)

    # Initializing an empty solution list.
    ga_sol = []

    # Using a genetic algorithm.
    # ga_sol = use_alg(random_grid)
    no_pmu = list(set(random_grid.nodes) - set(ga_sol))

    # tkinter gui
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry('800x600')
    root.title('Image Button Demo')



    fig = plt.figure(0)
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack()

    # Drawing nodes
    pos = nx.spring_layout(random_grid, seed=1234)
    nx.draw_networkx_nodes(random_grid, nodelist=ga_sol, node_color="green", pos=pos)
    nx.draw_networkx_nodes(random_grid, nodelist=no_pmu, node_color="red", pos=pos)

    # Drawing power grid model with electrical buses labels.
    nx.draw_networkx_edges(random_grid, pos=pos)

    # Drawing labels.
    labels_kv = list(random_grid.nodes)
    labels = {labels_kv[i]: labels_kv[i] for i in range(len(labels_kv))}
    nx.draw_networkx_labels(random_grid, labels=labels, pos=pos)



    # chaos Buttons
    # wybór min i max
    # losuj
    def rozpierdol():
        ga_sol = use_alg(random_grid)
        no_pmu = list(set(random_grid.nodes) - set(ga_sol))
        ax.clear()
        canvas.get_tk_widget().pack_forget()

        # Drawing nodes
        pos = nx.spring_layout(random_grid, seed=1234)
        nx.draw_networkx_nodes(random_grid, nodelist=ga_sol, node_color="green", pos=pos)
        nx.draw_networkx_nodes(random_grid, nodelist=no_pmu, node_color="red", pos=pos)

        # Drawing power grid model with electrical buses labels.
        nx.draw_networkx_edges(random_grid, pos=pos)

        # Drawing labels.
        labels_kv = list(random_grid.nodes)
        labels = {labels_kv[i]: labels_kv[i] for i in range(len(labels_kv))}
        nx.draw_networkx_labels(random_grid, labels=labels, pos=pos)
        canvas.get_tk_widget().pack()

    # odpal algorytm
    optimize_button = ttk.Button(
        master=root,
        text="optymalizuj",
        command=rozpierdol,
        compound=tk.BOTTOM
    )
    optimize_button.pack()







    root.mainloop()


if __name__ == '__main__':
    main()
