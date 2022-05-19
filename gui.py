import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx

import figure
from solution import OptimalSolution
from power_grid_models import RandomGrid
import genetic_algorithm


class GUI:
    def __init__(self):
        self.ga_params = {
            'max_iter': 200,
            'population_size': 100
        }
        self.min_buses, self.max_buses = 40, 50

        self.optimal_solution = False

        self.root = tk.Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self.power_grid = nx.Graph()

        self.figure = figure.Figure(self.power_grid, self.root)

        ttk.Button(self.frm, text="Optimize", command=lambda: self.__optimize()).grid(column=0, row=0)
        ttk.Button(self.frm, text="Random power grid", command=lambda: self.__randomize()).grid(column=1, row=0)
        ttk.Button(self.frm, text="Quit", command=self.root.quit).grid(column=2, row=0)

        # Current iteration label
        iteration_of_alg = 0
        var = tk.StringVar()
        var.set(f"0 / {self.ga_params['max_iter']}")
        self.label = tk.Label(self.root, textvariable=var)
        self.label.grid()

        self.root.mainloop()

    def __optimize(self):
        self.label.destroy()
        self.optimal_solution = OptimalSolution(self.power_grid, self.root, self.ga_params, self.figure)
        self.figure.update(self.power_grid, self.optimal_solution.solution)
        var = tk.StringVar()
        var.set(f"{self.ga_params['max_iter']} / {self.ga_params['max_iter']}")
        self.label = tk.Label(self.root, textvariable=var)
        self.label.grid()

    def __randomize(self):
        self.power_grid = RandomGrid(self.min_buses, self.max_buses)
        self.figure.update(self.power_grid, [])



