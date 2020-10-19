import tkinter as tk
import colors as c
import random


class Game(tk.Frame):
    def __init__(self):
        self.grid()
        self.master.title("2048 game")
        self.main_grid = tk.frame(self, bg=c.GRID_COLOR, bd=3, width=400, height=400)
        self.main_grid.grid(pady=(80, 0))
        self.make_GUI()
        self.start_game()
        self.master.bind("<left>",self.left)
        self.master.bind("<right>",self.right)
        self.master.bind("<up>",self.up)
        self.master.bind("<down>",self.down)
        self.mainloop()
    def make_GUI(self):
        #make grid
        self.cells=[]
        for i in range(4):
            row=[]
            for j in range(4):
                cell_frame=tk.frame(self.main_grid,bg=c.EMPTY_CELL_COLOR,width=100,height=100)
                cell_number=tk.Label(self.main_grid,bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i,column=j)
                cell_data={"frame":cell_frame,"data":cell_data}
                row.append(cell_data)
            self.cells.append(row)





