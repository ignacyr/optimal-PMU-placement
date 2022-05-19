import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx

import figure
from solution import OptimalSolution
from power_grid_models import RandomGrid


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self.power_grid = nx.Graph()

        self.figure = figure.Figure(self.power_grid, self.root)

        ttk.Button(self.frm, text="Optimize", command=lambda: self.__optimize()).grid(column=0, row=0)
        ttk.Button(self.frm, text="Random power grid", command=lambda: self.__randomize()).grid(column=1, row=0)
        ttk.Button(self.frm, text="Quit", command=self.root.quit).grid(column=2, row=0)

        self.root.mainloop()

    def __optimize(self):
        optimal_solution = OptimalSolution(self.power_grid)
        self.figure.update(self.power_grid, optimal_solution.solution)

    def __randomize(self):
        self.power_grid = RandomGrid(10, 12)
        self.figure.update(self.power_grid, [])



