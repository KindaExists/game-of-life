from board import Board
import visual


def start():
    board = Board(100, 50)
    visual.init_pygame(board)

if __name__ == '__main__':
    start()