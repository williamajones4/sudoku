"""This file is to define visualization functions for puzzles"""
import sys
import threading
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def visualize_sudoku(grid):
    """Visualizes a Sudoku grid using matplotlib."""
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(-.5, 9, 1), minor=False)
    ax.set_yticks(np.arange(-.5, 9, 1), minor=False)
    ax.grid(which='major', color='k', linestyle='-', linewidth=2)
    ax.set_xticks(np.arange(-.5, 9, 3), minor=False)
    ax.set_yticks(np.arange(-.5, 9, 3), minor=False)
    ax.grid(which='major', color='k', linestyle='-', linewidth=4)

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                ax.text(i, j, grid[i][j], ha="center", va="center", fontsize=20)

    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(8.5, -0.5) # Invert y axis for correct row display
    thread = threading.Thread(target=plt.show(), daemon=True)
    thread.start()

if __name__ == "__main__":
    visualize_sudoku(pd.read_csv(sys.argv[1], header=None))
