import numpy as np
from numpy.random import default_rng
import tkinter as tk
from tkinter import ttk
import networkx as nx


class GeneticAlgorithmOPP:
    def __init__(self, grid, ga_params, root, figure, frm2):
        self.adjacency_matrix = nx.to_numpy_array(grid)
        np.fill_diagonal(self.adjacency_matrix, 1)

        # For GUI
        self.grid = grid
        self.figure = figure
        self.root = root
        self.var = tk.StringVar()
        self.var.set(f"0 / {ga_params['max_iter']}")
        self.label = tk.Label(root, textvariable=self.var)
        self.label.grid()
        self.break_alg = False
        ttk.Button(self.root, text="Stop", command=lambda: self.__break_alg(), padding=10).place(x=800, y=750)
        # For GUI

        if len(self.adjacency_matrix) == 0:
            self.solution = []
            return

        self.number_of_buses = self.adjacency_matrix[0].size

        self.max_iter = ga_params['max_iter']
        self.population_size = ga_params['population_size']
        self.mutation_strength = ga_params['mutation_strength']

        self.current_population = []
        self.ranked_population = []
        self.best_population = []
        self.final_solution = np.array([])

        self.frm2 = frm2

        self.mutation_strength_entry = tk.StringVar()
        self.mutation_strength_entry.set(f"{len(self.grid)-1} / {len(self.grid)}")
        tk.Label(self.frm2, textvariable=self.mutation_strength_entry, width=15).grid(column=4, row=3)

    def start(self):
        self.__generate_first_generation()
        self.__mainloop()
        return self.final_solution

    def __break_alg(self):
        self.break_alg = True

    def __generate_first_generation(self):
        self.rng = default_rng()
        while not self.current_population:
            for i in range(self.population_size):
                n_of_pmu = self.number_of_buses - self.rng.choice(2)
                self.current_population.append(self.rng.choice(self.number_of_buses, n_of_pmu, replace=False) + 1)

    def __target(self, placement):
        number_of_pmu = placement.size
        for a in range(self.adjacency_matrix[0].size):
            bus_connections = np.add(self.adjacency_matrix[a].nonzero(), 1)
            if not np.any(np.intersect1d(placement, bus_connections)):  # Has that bus any connection?
                return -1
        return number_of_pmu

    def __fitness(self, placement):
        number_of_pmu = self.__target(placement)
        if number_of_pmu < 0:
            return -1
        points = 0
        for pmu in placement:
            points = points + 1 / np.sum(self.adjacency_matrix[pmu - 1])
        return points

    def __selection(self):
        for p in self.current_population:
            self.ranked_population.append((self.__fitness(p), p))
        self.ranked_population = list(filter(lambda x: x[0] > 0, self.ranked_population))
        self.ranked_population.sort(key=lambda y: y[0])
        if self.ranked_population:
            if 0 < self.__fitness(self.ranked_population[0][1]) < self.__fitness(self.final_solution):
                self.final_solution = self.ranked_population[0][1]
            if not self.final_solution.any():
                self.final_solution = self.ranked_population[0][1]
            self.best_population = self.ranked_population[:self.population_size // 10]

    def __crossover(self):
        best_buses = np.array([], dtype=int)
        size_of_best_solutions = np.array([], dtype=int)
        for bp in self.best_population:
            best_buses = np.append(best_buses, bp[1])
            size_of_best_solutions = np.append(size_of_best_solutions, bp[1].size)

        best_buses = self.__mutation(best_buses)

        new_gen = []
        while len(new_gen) < self.population_size:
            # size = np.min(size_of_best_solutions) - self.rng.integers(2)  # half of numbers is smaller
            size = np.min(size_of_best_solutions) - (1 - bool(int(self.rng.integers(6))))  # one smaller number every 5 numbers
            element = self.rng.choice(best_buses, size, replace=False)  # replace change to False!!!!!!!!!!!!
            element = np.unique(element.astype(int))
            if self.__fitness(element) > 0:  # Check if observability is
                new_gen.append(element)
        self.current_population = new_gen

    def __mutation(self, best_buses):
        for i in range(round(len(self.best_population) * self.mutation_strength)):
            best_buses = np.append(best_buses, self.rng.integers(self.number_of_buses) + 1)
        return best_buses

    def __single_iteration(self, i):
        self.__selection()
        self.__crossover()

        # For GUI
        self.figure.update(self.grid, self.final_solution)
        self.var.set(f"Iteration: {i + 1} / {self.max_iter}")
        self.root.update_idletasks()
        # For GUI

        self.ranked_population = []
        self.best_population = []

    def __mainloop(self):
        for i in range(self.max_iter):
            self.__single_iteration(i)
            self.root.update()
            if self.break_alg:
                break
            self.mutation_strength_entry.set(f"{len(self.final_solution)} / {len(self.grid)}")

        self.label.destroy()



