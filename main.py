from enum import auto

import numpy as np
from strenum import StrEnum

zeroes = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

easy_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

easy_solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

expert_grid = [
    [0, 0, 0, 0, 5, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [6, 8, 3, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 8, 0, 7, 0, 0, 6, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 5],
    [0, 5, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 1, 6, 0, 0],
    [0, 7, 0, 0, 0, 6, 0, 0, 3]
]

expert_solution = [
    [4, 2, 7, 6, 5, 8, 3, 1, 9],
    [9, 1, 5, 4, 3, 2, 7, 8, 6],
    [6, 8, 3, 9, 1, 7, 4, 5, 2],
    [1, 3, 2, 8, 6, 5, 9, 7, 4],
    [5, 9, 8, 3, 7, 4, 2, 6, 1],
    [7, 6, 4, 1, 2, 9, 8, 3, 5],
    [2, 5, 6, 7, 4, 3, 1, 9, 8],
    [3, 4, 9, 5, 8, 1, 6, 2, 7],
    [8, 7, 1, 2, 9, 6, 5, 4, 3]
]

evil_grid = [
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 9, 0, 5, 0, 1, 0, 8, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 7],
    [0, 4, 0, 9, 0, 8, 0, 5, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 3, 0],
    [7, 0, 0, 1, 0, 3, 0, 0, 5],
    [0, 1, 0, 0, 6, 0, 0, 0, 0]
]

init_grid = easy_grid
solution_grid = easy_solution

grid = np.empty([9, 9], dtype=object)

cells_left = 81
cells_left_old = cells_left

iterations = 0


class State(StrEnum):
    SET = auto()
    GUESSING = auto()
    GUESSED = auto()


class Cell:
    _value = 0

    possible_values: list[int]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        global cells_left
        if val != 0 and val != solution_grid[self.x][self.y]:
            raise ValueError(f'Incorrect guess for cell ({self.x}, {self.y})')
        if val not in self.possible_values:
            raise ValueError(f"{val} is not present in possible values")
        else:
            if val != 0:
                self.possible_values = []
                cells_left -= 1
            self._value = val

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.possible_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __repr__(self) -> str:
        return str(self.value) if self.value else '.'

    def __int__(self) -> int:
        return self.value


def round_3(i):
    return 3 * (i // 3)


def print_found(cell):
    print(f'value found: {cell.value} in cell ({cell.x}, {cell.y})')
    print(grid)


def init():
    for i in range(9):
        for j in range(9):
            cell = Cell(i, j)
            cell.value = init_grid[i][j]
            # cell.value = 9 * i + j + 1
            grid[i][j] = cell
    print(grid)


def app():
    global cells_left, cells_left_old, iterations

    init()

    improvement = 0

    while cells_left_old != cells_left or improvement > 0:
        improvement = 0
        cells_left_old = cells_left

        for i in range(9):
            for j in range(9):
                cell = grid[i][j]
                row = grid[i].astype(int)
                col = grid.transpose()[j].astype(int)
                grid_9 = grid[round_3(i):round_3(i) + 3, round_3(j):round_3(j) + 3].flatten().astype(int)


                for x in row:
                    if x in cell.possible_values:
                        cell.possible_values.remove(x)

                for x in col:
                    if x in cell.possible_values:
                        cell.possible_values.remove(x)

                for x in grid_9:
                    if x in cell.possible_values:
                        cell.possible_values.remove(x)

                if len(cell.possible_values) == 1:
                    cell.value = cell.possible_values[0]
                    print_found(cell)

        for i in range(9):
            for j in range(9):
                cell = grid[i][j]
                row = grid[i]
                col = grid.transpose()[j]
                grid_9 = grid[round_3(i):round_3(i) + 3, round_3(j):round_3(j) + 3].flatten()

                stats = {
                    'row': np.empty(10, dtype=object),
                    'col': np.empty(10, dtype=object),
                    'grid_9': np.empty(10, dtype=object)
                }

                for p in range(0, 10):
                    stats['row'][p] = []
                    stats['col'][p] = []
                    stats['grid_9'][p] = []

                for c in row:
                    for pv in c.possible_values:
                        stats['row'][pv].append(c)

                for c in col:
                    for pv in c.possible_values:
                        stats['col'][pv].append(c)

                for c in grid_9:
                    for pv in c.possible_values:
                        stats['grid_9'][pv].append(c)

                for k in range(1, 10):
                    # for direction in ['row', 'col', 'grid_9']:
                    if len(stats['row'][k]) == 1 and \
                            len(stats['col'][k]) == 1 and \
                            len(stats['grid_9'][k]) == 1:
                        k_: Cell = stats['row'][k][0]
                        # print(k_)
                        # print(k_)
                        if k in k_.possible_values:
                            print(f'Possible value: {k} in cell ({k_.x}, {k_.y})')
                            print_possible_values()
                            k_.value = k
                            pass

        # print_possible_values()

        # When possible values are only found on one row / column in a subgrid, remove these possible values from the
        # rest of the row / column.

        # For all subgrids
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                grid_9 = grid[round_3(i):round_3(i) + 3, round_3(j):round_3(j) + 3]

                # For all numbers
                for z in range(1, 10):
                    skip = False
                    rows = []
                    cols = []

                    # For all cells in the subgrid
                    for x in range(3):
                        for y in range(3):
                            cell = grid_9[x][y]
                            if cell.value == z:
                                skip = True
                            if z in cell.possible_values:
                                rows.append(cell.x)
                                cols.append(cell.y)
                    if skip:
                        continue

                    rows = np.unique(np.array(rows))
                    cols = np.unique(np.array(cols))
                    if len(rows) == 1:
                        row = rows[0]
                        skip = False
                        # for cell in grid[row]:
                        #     if cell.value == z:
                        #         skip = True
                        if not skip:
                            print(f'In subgrid ({i//3}, {j//3}): number {z} only found on row {row}')
                            for cell in grid[row]:
                                if round_3(cell.y) != j:
                                    if z in cell.possible_values:
                                        improvement += 1
                                        print(f'> Removing {z} from the possible_values of ({cell.x}, {cell.y})')
                                        cell.possible_values.remove(z)
                    if len(cols) == 1:
                        col = cols[0]
                        skip = False
                        # for cell in grid.T[col]:
                        #     if cell.value == z:
                        #         skip = True
                        if not skip:
                            print(f'In subgrid ({i//3}, {j//3}): number {z} only found on col {col}')
                            for cell in grid.T[col]:
                                if round_3(cell.x) != i:
                                    if z in cell.possible_values:
                                        improvement += 1
                                        print(f'> Removing {z} from the possible_values of ({cell.x}, {cell.y})')
                                        cell.possible_values.remove(z)

        print_possible_values()

        if cells_left != 0:
            iterations += 1
        else:
            break

    if cells_left == 0:
        print(f"Grid solved in {iterations} iterations !")
    else:
        print(f'Solving failed, cells left: {cells_left}')

    print(grid)
    print_possible_values()
    print(grid)


def pr(k):
    print(k, end='')


kk = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)


def print_possible_values():
    for i in range(9):
        for ki in kk:
            for j in range(9):
                cell = grid[i][j]
                for k in ki:
                    if k in cell.possible_values:
                        pr(k)
                    else:
                        pr(' ')
                pr('||' if j % 3 == 2 else '|')
            print('')
        print(('=' if i % 3 == 2 else '-') * (4 * 9 + 3))
    print('')


if __name__ == '__main__':
    app()
