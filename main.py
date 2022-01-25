import time

# Conway's Game of life rules from Wikipedia:
# 1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2) Any live cell with two or three live neighbours lives on to the next generation.
# 3) Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# My First approach to this is brute-force and iterating over every cell
# However, I believe the more optimized approach involves keeping
# all alive Cells in an array and creating computations off that
DIRECTIONS = [(1, 0),
              (-1, 0),
              (0, 1),
              (0, -1),
              (1, 1),
              (-1, 1),
              (1, -1),
              (-1, -1)]


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
        self.alive_cell_positions = []


    def get_cell(self, x, y):
        return self.board[y][x]

    def wake_up_cell(self, x, y):
        cell = self.get_cell(x, y)
        cell.wake_up()
        self.alive_cell_positions.append((x, y))

    def kill_cell(self, x, y):
        cell = self.get_cell(x, y)
        cell.kill()
        self.alive_cell_positions.remove((x, y))

    def toggle_cell(self, x, y):
        cell = self.get_cell(x, y)
        cell.toggle_state()
        if cell.alive:
            self.alive_cell_positions.append((x, y))
        else:
            self.alive_cell_positions.remove((x, y))


    def get_neighbor_positions(self, x, y):
        position = (x, y)

        potential_neighbor_positions = [tuple([sum(coordinate) for coordinate in zip(position, direction)]) for direction in DIRECTIONS]
        neighbor_positions = []

        for potential_position in potential_neighbor_positions:
            if potential_position[0] in range(self.bounds[0]) and potential_position[1] in range(self.bounds[1]):
                neighbor_positions.append(potential_position)

        return neighbor_positions


    def next_frame(self):
        changes = []
        counts = {}
        for cell_position in self.alive_cell_positions:
            neighbor_positions = self.get_neighbor_positions(*cell_position)
            for neighbor_position in neighbor_positions:
                counts[neighbor_position] = counts.get(neighbor_position, 0) + 1

        for cell_position, count in counts.items():
            cell = self.get_cell(*cell_position)
            if cell.alive:
                if count < 2:
                    changes.append([cell_position, False])
                if count > 3:
                    changes.append([cell_position, False])
            else:
                if count == 3:
                    changes.append([cell_position, True])

        self.__apply_changes(changes)

    def __apply_changes(self, changes):
        for change in changes:
            position = change[0]
            is_alive = change[1]
            if is_alive:
                self.wake_up_cell(*position)
            else:
                self.kill_cell(*position)


    def __str__(self):
        str_builder = ''
        str_builder += f'  {" ".join([str(num % 10) for num in range(self.bounds[0])])}\n'
        str_builder += '\n'.join([f'{i % 10} {" ".join([str(cell) for cell in row])}' for i, row in enumerate(self.board)])
        return str_builder



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
