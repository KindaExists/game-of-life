from pip import main
from board import Board
import time

# Conway's Game of life rules from Wikipedia:
# 1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2) Any live cell with two or three live neighbours lives on to the next generation.
# 3) Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# My First approach to this is brute-force and iterating over every cell
# However, I believe the more optimized approach involves keeping
# all alive Cells in an array and creating computations off that


def start():
    board = Board(20, 20)
    board.toggle_cell(4, 6)
    board.toggle_cell(5, 7)
    board.toggle_cell(6, 7)
    board.toggle_cell(4, 8)
    board.toggle_cell(5, 8)

    board.toggle_cell(13, 6)
    board.toggle_cell(12, 7)
    board.toggle_cell(11, 7)
    board.toggle_cell(13, 8)
    board.toggle_cell(12, 8)
    main_loop(board)

def main_loop(board):
    while True:
        print(board)
        time.sleep(0.2)
        board.next_frame()


start()
