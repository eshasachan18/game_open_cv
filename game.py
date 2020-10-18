
import tkinter as tk
import random
import colors as c


class Game(tk.frame):
    def __init__(self):
        self.grid()
        self.master.title("2048 game")
        self.main_grid = tk.frame(self, bg=c.GRID_COLOR, bd=3, width=400, height=400)
        self.main_grid.grid(pady=(80, 0))
