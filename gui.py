import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt

import figure
from solution import OptimalSolution
from power_grid_models import RandomGrid, UserDefinedGrid


class GUI:
    def __init__(self):
        self.ga_params = {
            'max_iter': 0,
            'population_size': 50,
            'mutation_strength': 1.0
        }
        self.min_buses, self.max_buses = 8, 10

        self.root = tk.Tk()
        self.root.title('Optimal PMU placement with genetic algorithm')
        self.root.resizable(height=False, width=False)
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self.power_grid = nx.Graph()

        self.figure = figure.Figure(self.power_grid, self.root)

        ttk.Button(self.frm, text="Add nodes quantity:", command=lambda: self.__add_nodes_number(), padding=10).grid(column=0, row=0)
        ttk.Label(self.frm, text="           ").grid(column=1, row=0)
        ttk.Button(self.frm, text="Add a connection:", command=lambda: self.__add_connection(), padding=10).grid(column=2, row=0)

        ttk.Label(self.frm, text="           ").grid(column=1, row=1)
        self.nodes_number_entry = tk.StringVar()
        ttk.Entry(self.frm, textvariable=self.nodes_number_entry, width=10).place(x=37, y=45)
        self.connection1_entry = tk.StringVar()
        ttk.Entry(self.frm, textvariable=self.connection1_entry, width=6).place(x=215, y=45)
        self.connection2_entry = tk.StringVar()
        ttk.Entry(self.frm, textvariable=self.connection2_entry, width=6).place(x=275, y=45)

        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm2.grid()

        ttk.Button(self.frm2, text="Random power grid", command=lambda: self.__randomize(), padding=10).grid(column=0, row=1)
        ttk.Label(self.frm2, text="Max number of buses:").grid(column=1, row=0)
        self.max_buses_entry = tk.StringVar()
        ttk.Entry(self.frm2, textvariable=self.max_buses_entry, width=15).grid(column=1, row=1)
        ttk.Label(self.frm2, text="Min number of buses:").grid(column=1, row=2)
        self.min_buses_entry = tk.StringVar()
        ttk.Entry(self.frm2, textvariable=self.min_buses_entry, width=15).grid(column=1, row=3)

        ttk.Button(self.frm2, text="Optimize", command=lambda: self.__optimize(), padding=10).grid(column=2, row=1)
        ttk.Label(self.frm2, text="Generations:").grid(column=3, row=0)
        self.max_iter_entry = tk.StringVar()
        ttk.Entry(self.frm2, textvariable=self.max_iter_entry, width=15).grid(column=3, row=1)
        ttk.Label(self.frm2, text="Population size:").grid(column=3, row=2)
        self.population_size_entry = tk.StringVar()
        ttk.Entry(self.frm2, textvariable=self.population_size_entry, width=15).grid(column=3, row=3)
        ttk.Label(self.frm2, text="Mutation:").grid(column=4, row=0)
        self.mutation_strength_entry = tk.StringVar()
        ttk.Entry(self.frm2, textvariable=self.mutation_strength_entry, width=15).grid(column=4, row=1)

        var = tk.StringVar()
        var.set(f"Iteration: 0 / {self.ga_params['max_iter']}")
        self.label = tk.Label(self.root, textvariable=var)
        self.label.grid()

        self.root.mainloop()

    def __optimize(self):
        self.ga_params['max_iter'] = int(self.max_iter_entry.get())
        self.ga_params['population_size'] = int(self.population_size_entry.get())
        self.ga_params['mutation_strength'] = float(self.mutation_strength_entry.get())
        self.label.destroy()
        self.optimal_solution = OptimalSolution(self.power_grid, self.root, self.ga_params, self.figure)
        self.figure.update(self.power_grid, self.optimal_solution.solution)
        var = tk.StringVar()
        var.set(f"Iteration: {self.ga_params['max_iter']} / {self.ga_params['max_iter']}")
        self.label = tk.Label(self.root, textvariable=var)
        self.label.grid()

    def __randomize(self):
        self.min_buses = int(self.min_buses_entry.get())
        self.max_buses = int(self.max_buses_entry.get())
        self.power_grid = RandomGrid(self.min_buses, self.max_buses)
        self.figure.update(self.power_grid, [])

    def __add_nodes_number(self):
        self.power_grid = UserDefinedGrid(int(self.nodes_number_entry.get()))
        self.figure.update(self.power_grid, [])

    def __add_connection(self):
        self.power_grid.add_edge(int(self.connection1_entry.get()), int(self.connection2_entry.get()))
        self.figure.update(self.power_grid, [])




