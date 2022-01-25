import time

# Conway's Game of life rules from Wikipedia:
# 1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2) Any live cell with two or three live neighbours lives on to the next generation.
# 3) Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# My First approach to this is brute-force and iterating over every cell
# However, I believe the more optimized approach involves keeping
# all alive Cells in an array and creating computations off that

class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def toggle_state(self):
        self.alive = not self.alive

    def wake_up(self):
        self.alive = True

    def kill(self):
        self.alive = False

    def __str__(self):
        if self.alive:
            return '#'
        else:
            return '.'


class Board:
    def __init__(self, width, height):
        self.bounds = (width, height)
        self.board = [[Cell() for _ in range(width)] for _ in range(height)]

    def printBoard(self):
        print('  ' + ' '.join([str(num % 10) for num in range(20)]))
        for index, row in enumerate(self.board):
            print(index % 10, end=' ')
            for cell in row:
                print(cell, end=' ')
            print()

    def get_cell(self, x, y):
        return self.board[y][x]

    def get_cell_neighbors(self, x, y):
        pos = (x, y)
        neighbor_rel = [(1, 0),
                        (-1, 0),
                        (0, 1),
                        (0, -1),
                        (1, 1),
                        (-1, 1),
                        (1, -1),
                        (-1, -1)]
        potential_neighbors = [tuple([sum(coord) for coord in zip(pos, rel_pos)]) for rel_pos in neighbor_rel]
        neighbors = []

        for neighbor_pos in potential_neighbors:
            if neighbor_pos[0] in range(self.bounds[0]) and neighbor_pos[1] in range(self.bounds[1]):
                neighbor = self.get_cell(neighbor_pos[0], neighbor_pos[1])
                neighbors.append(neighbor)

        return neighbors

    def get_alive_neighbors(self, x, y):
        neighbors = self.get_cell_neighbors(x, y)
        alive_neighbors = []

        for neighbor in neighbors:
            if neighbor.alive:
                alive_neighbors.append(neighbor)

        return alive_neighbors

    def count_alive_neighbors(self, x, y):
        return len(self.get_alive_neighbors(x, y))

    def next_frame(self):
        changes = []
        for x in range(self.bounds[0]):
            for y in range(self.bounds[1]):
                current_cell = self.get_cell(x, y)
                alive_neighbor_count = self.count_alive_neighbors(x, y)

                if current_cell.alive:
                    if alive_neighbor_count < 2:
                        changes.append([current_cell, False])
                    if alive_neighbor_count > 3:
                        changes.append([current_cell, False])
                else:
                    if alive_neighbor_count == 3:
                        changes.append([current_cell, True])

        for change in changes:
            cell = change[0]
            is_alive = change[1]
            if is_alive:
                cell.wake_up()
            else:
                cell.kill()


def start():
    board = Board(20, 20)
    board.get_cell(4, 6).toggle_state()
    board.get_cell(5, 7).toggle_state()
    board.get_cell(6, 7).toggle_state()
    board.get_cell(4, 8).toggle_state()
    board.get_cell(5, 8).toggle_state()

    board.get_cell(13, 6).toggle_state()
    board.get_cell(12, 7).toggle_state()
    board.get_cell(11, 7).toggle_state()
    board.get_cell(13, 8).toggle_state()
    board.get_cell(12, 8).toggle_state()


    board.printBoard()
    print(board.count_alive_neighbors(7, 7))
    main_loop(board)


def main_loop(board):
    while True:
        board.printBoard()
        time.sleep(0.2)
        board.next_frame()


start()
