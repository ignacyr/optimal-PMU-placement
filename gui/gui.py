import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


"""
To use write:
root = GUI()
root.mainloop()
"""


class GUI:
    def __init__(self, figure: plt.Figure, optimize_command, randomize_command):
        self.root = tk.Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        ttk.Button(self.frm, text="Optimize", command=self.__optimize()).grid(column=0, row=0)
        ttk.Button(self.frm, text="Random power grid", command=self.__randomize()).grid(column=1, row=0)
        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=2, row=0)

        self.figure = figure
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().grid()

        self.optimize_command = optimize_command
        self.randomize_command = randomize_command

        self.root.mainloop()

    def __optimize(self, grid):
        optimal_solution = OptimalSolution(grid)

    def __randomize(self):
        pass


fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
gui = GUI(fig)


