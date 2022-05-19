import numpy as np
from numpy.random import default_rng
import tkinter as tk
import networkx as nx


class GeneticAlgorithmOPP:
    def __init__(self, grid, ga_params, root, figure):
        self.adjacency_matrix = nx.to_numpy_array(grid)
        np.fill_diagonal(self.adjacency_matrix, 1)

        # For GUI
        self.grid = grid
        self.figure = figure
        self.root = root
        self.var = tk.StringVar()
        print(ga_params)
        self.var.set(f"0 / {ga_params['max_iter']}")
        self.label = tk.Label(root, textvariable=self.var)
        self.label.grid()
        # For GUI

        if len(self.adjacency_matrix) == 0:
            self.solution = []
            return

        self.number_of_buses = self.adjacency_matrix[0].size

        self.max_iter = ga_params['max_iter']
        self.population_size = ga_params['population_size']

        self.current_population = []
        self.ranked_population = []
        self.best_population = []
        self.final_solution = np.array([0])

        self.best_buses = np.array([], dtype=int)
        self.size_of_best_solution = np.array([], dtype=int)

    def start(self):
        self.__generate_first_generation()
        self.__mainloop()
        return self.final_solution

    def __generate_first_generation(self):
        self.rng = default_rng()
        while not self.current_population:
            for i in range(self.population_size):
                n_of_pmu = self.rng.choice(self.number_of_buses) + 1
                self.current_population.append(self.rng.choice(self.number_of_buses, n_of_pmu, replace=False) + 1)

    def __target(self, placement):
        number_of_pmu = placement.size
        for a in range(self.adjacency_matrix[0].size):
            bus_connections = np.add(self.adjacency_matrix[a].nonzero(), 1)
            if not np.any(np.intersect1d(placement, bus_connections)):  # Has that bus any connection?
                return -1
        return number_of_pmu

    def __fitness(self, placement, adjacency_m):
        number_of_pmu = self.__target(placement)
        if number_of_pmu < 0:
            return -1
        points = 0
        for pmu in placement:
            points = points + 1 / np.sum(adjacency_m[pmu - 1])
        return points

    def __selection(self):
        for p in self.current_population:
            self.ranked_population.append((self.__fitness(p, self.adjacency_matrix), p))
        self.ranked_population.sort(key=lambda y: y[0])
        self.ranked_population = list(filter(lambda x: x[0] > 0, self.ranked_population))
        if self.ranked_population:
            if 0 < self.__fitness(self.ranked_population[0][1], self.adjacency_matrix) < self.__fitness(self.final_solution, self.adjacency_matrix):
                self.final_solution = self.ranked_population[0][1]
            if not self.final_solution.any():
                self.final_solution = self.ranked_population[0][1]
            self.best_population = self.ranked_population[:self.population_size // 10]

    def __crossover(self):
        self.best_buses = np.array([], dtype=int)
        self.size_of_best_solution = np.array([], dtype=int)
        for bp in self.best_population:
            self.best_buses = np.append(self.best_buses, bp[1])
            self.size_of_best_solution = np.append(self.size_of_best_solution, bp[1].size)
            self.best_buses = np.append(self.best_buses, self.rng.integers(self.number_of_buses) + 1)  # random bus as a mutation
        # have to add better mutations
        new_gen = []
        while len(new_gen) < self.population_size:
            size = np.min(self.size_of_best_solution) - self.rng.integers(2)
            element = self.rng.choice(self.best_buses, size, replace=True)  # replace change to False!!!!!!!!!!!!
            element = np.unique(element.astype(int))
            new_gen.append(element)
        self.current_population = new_gen

    def __mutation(self):
        pass

    def __mainloop(self):
        for i in range(self.max_iter):
            self.__selection()
            self.__crossover()
            self.__mutation()

            # For GUI
            self.figure.update(self.grid, self.final_solution)
            self.var.set(f"Iteration: {i + 1} / {self.max_iter}")
            self.root.update_idletasks()
            # For GUI

            # na końcu zerować zmienne!!!

        self.label.destroy()



