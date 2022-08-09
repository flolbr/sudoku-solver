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

nyt_grid = [
    [6, 3, 0, 0, 0, 0, 0, 8, 1],
    [0, 2, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 1, 7, 4, 3, 0],
    [0, 9, 6, 4, 0, 0, 5, 7, 0],
    [0, 0, 0, 7, 6, 2, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 6, 0, 0],
    [0, 6, 0, 0, 2, 0, 0, 0, 0],
    [3, 0, 9, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9],
]

nyt_solution = [
    [6, 3, 7, 2, 5, 4, 9, 8, 1],
    [1, 2, 4, 8, 9, 3, 7, 5, 6],
    [9, 5, 8, 6, 1, 7, 4, 3, 2],
    [2, 9, 6, 4, 8, 1, 5, 7, 3],
    [5, 4, 3, 7, 6, 2, 1, 9, 8],
    [7, 8, 1, 9, 3, 5, 6, 2, 4],
    [4, 6, 5, 3, 2, 9, 8, 1, 7],
    [3, 7, 9, 1, 4, 8, 2, 6, 5],
    [8, 1, 2, 5, 7, 6, 3, 4, 9],
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

evil_solution = [
    [1, 8, 3, 6, 9, 4, 5, 7, 2],
    [4, 7, 5, 3, 8, 2, 9, 1, 6],
    [2, 9, 6, 5, 7, 1, 3, 8, 4],
    [8, 3, 2, 4, 5, 6, 1, 9, 7],
    [6, 4, 7, 9, 1, 8, 2, 5, 3],
    [9, 5, 1, 2, 3, 7, 4, 6, 8],
    [5, 2, 8, 7, 4, 9, 6, 3, 1],
    [7, 6, 9, 1, 2, 3, 8, 4, 5],
    [3, 1, 4, 8, 6, 5, 7, 2, 9]
]

evil2_grid = [
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 0, 7, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 2, 7, 0, 0],
    [3, 0, 4, 0, 0, 5, 0, 0, 8],
    [0, 9, 0, 0, 3, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 4, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 5],
    [7, 0, 1, 0, 2, 0, 0, 8, 0]
]

evil2_solution = [
    [9, 7, 2, 4, 1, 3, 8, 5, 6],
    [8, 5, 3, 9, 7, 6, 4, 1, 2],
    [4, 1, 6, 8, 5, 2, 7, 3, 9],
    [3, 6, 4, 7, 9, 5, 1, 2, 8],
    [1, 9, 8, 2, 3, 4, 5, 6, 7],
    [5, 2, 7, 1, 6, 8, 9, 4, 3],
    [6, 4, 5, 3, 8, 7, 2, 9, 1],
    [2, 8, 9, 6, 4, 1, 3, 7, 5],
    [7, 3, 1, 5, 2, 9, 6, 8, 4]
]

init_grid = evil2_grid
solution_grid = evil2_solution
check_solution = True

grid = np.empty([9, 9], dtype=object)

cells_left = 81
cells_left_old = cells_left

iterations = 0

improvement = 0


class State(StrEnum):
    SET = auto()
    GUESSING = auto()
    GUESSED = auto()


class Cell:
    _value = 0

    possible_values: list[int]

    def remove_possible_value(self, value):
        self.possible_values.remove(value)

        if len(self.possible_values) == 1:
            self.value = self.possible_values[0]
            print_found(self)

    def update_surrounding(self):
        global improvement
        row = grid[self.x]
        col = grid.transpose()[self.y]
        grid_9 = grid[round_3(self.x):round_3(self.x) + 3, round_3(self.y):round_3(self.y) + 3].flatten()

        # Remove values already in the row / column / subgrid from the possible values
        # if self.value != 0:
        for x in row.astype(int):
            if x in self.possible_values:
                self.remove_possible_value(x)

        for x in col.astype(int):
            if x in self.possible_values:
                self.remove_possible_value(x)

        for x in grid_9.astype(int):
            if x in self.possible_values:
                self.remove_possible_value(x)

        # If the value is set, remove this value from the possible values of the surrounding cells
        if self.value != 0:
            for x in row:
                if self.value in x.possible_values:
                    x.remove_possible_value(self.value)

            for x in col:
                if self.value in x.possible_values:
                    x.remove_possible_value(self.value)

            for x in grid_9:
                if self.value in x.possible_values:
                    x.remove_possible_value(self.value)

        # for i in [0, 3, 6]:
        #     for j in [0, 3, 6]:
        #         # grid_9 = grid[round_3(i):round_3(i) + 3, round_3(j):round_3(j) + 3]
        #
        #         # For all numbers
        #         for z in range(1, 10):
        #             skip = False
        #             rows = []
        #             cols = []
        #
        #             # For all cells in the subgrid
        #             for x in range(3):
        #                 for y in range(3):
        #                     cell = grid_9[x][y]
        #                     if cell.value == z:
        #                         skip = True
        #                     if z in cell.possible_values:
        #                         rows.append(cell.x)
        #                         cols.append(cell.y)
        #             if skip:
        #                 continue
        #
        #             rows = np.unique(np.array(rows))
        #             cols = np.unique(np.array(cols))
        #             if len(rows) == 1:
        #                 row = rows[0]
        #                 skip = False
        #                 # for cell in grid[row]:
        #                 #     if cell.value == z:
        #                 #         skip = True
        #                 if not skip:
        #                     print(f'In subgrid ({i//3}, {j//3}): number {z} only found on row {row}')
        #                     for cell in grid[row]:
        #                         if round_3(cell.y) != j:
        #                             if z in cell.possible_values:
        #                                 improvement += 1
        #                                 print(f'> Removing {z} from the possible_values of ({cell.x}, {cell.y})')
        #                                 cell.possible_values.remove(z)
        #             if len(cols) == 1:
        #                 col = cols[0]
        #                 skip = False
        #                 # for cell in grid.T[col]:
        #                 #     if cell.value == z:
        #                 #         skip = True
        #                 if not skip:
        #                     print(f'In subgrid ({i//3}, {j//3}): number {z} only found on col {col}')
        #                     for cell in grid.T[col]:
        #                         if round_3(cell.x) != i:
        #                             if z in cell.possible_values:
        #                                 improvement += 1
        #                                 print(f'> Removing {z} from the possible_values of ({cell.x}, {cell.y})')
        #                                 cell.possible_values.remove(z)

    def force_value(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        global cells_left
        if check_solution and val != 0 and val != solution_grid[self.x][self.y]:
            raise ValueError(f'Incorrect guess for cell ({self.x}, {self.y})')
        if val not in self.possible_values:
            raise ValueError(f"{val} is not present in possible values")
        else:
            if val != 0:
                self.possible_values = []
                cells_left -= 1
            self._value = val
            self.update_surrounding()

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
    global cells_left, cells_left_old
    for i in range(9):
        for j in range(9):
            cell = Cell(i, j)
            cell.force_value(init_grid[i][j])
            if cell.value != 0:
                cell.possible_values = []
                cells_left -= 1
            # cell.value = 9 * i + j + 1
            grid[i][j] = cell
    print(grid)
    cells_left_old = cells_left


def app():
    global cells_left, cells_left_old, iterations, improvement

    init()

    improvement = 1

    # while improvement > 0:
    while cells_left_old != cells_left or improvement > 0:
        improvement = 0
        # improvement -= 1
        cells_left_old = cells_left

        for i in range(9):
            for j in range(9):
                cell: Cell = grid[i][j]
                cell.update_surrounding()
                # row = grid[i].astype(int)
                # col = grid.transpose()[j].astype(int)
                # grid_9 = grid[round_3(i):round_3(i) + 3, round_3(j):round_3(j) + 3].flatten().astype(int)
                #
                #
                # for x in row:
                #     if x in cell.possible_values:
                #         cell.remove_possible_value(x)
                #
                # for x in col:
                #     if x in cell.possible_values:
                #         cell.remove_possible_value(x)
                #
                # for x in grid_9:
                #     if x in cell.possible_values:
                #         cell.remove_possible_value(x)

                # if len(cell.possible_values) == 1:
                #     cell.value = cell.possible_values[0]
                #     print_found(cell)

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
                            print(f'In subgrid ({i // 3}, {j // 3}): number {z} only found on row {row}')
                            for cell in grid[row]:
                                if round_3(cell.y) != j:
                                    if z in cell.possible_values:
                                        improvement += 1
                                        print(f'> Removing {z} from the possible_values of ({cell.x}, {cell.y})')
                                        cell.remove_possible_value(z)
                    if len(cols) == 1:
                        col = cols[0]
                        skip = False
                        # for cell in grid.T[col]:
                        #     if cell.value == z:
                        #         skip = True
                        if not skip:
                            print(f'In subgrid ({i // 3}, {j // 3}): number {z} only found on col {col}')
                            for cell in grid.T[col]:
                                if round_3(cell.x) != i:
                                    if z in cell.possible_values:
                                        improvement += 1
                                        print(f'> Removing {z} from the possible_values of ({cell.x}, {cell.y})')
                                        cell.remove_possible_value(z)

        print_possible_values()

        for i in range(1, 10):
            solve_twos(i)

        print_possible_values()

        if cells_left != 0:
            iterations += 1
        else:
            break

    if cells_left == 0:
        print(f"Grid solved in {iterations} iterations !")
    else:
        print(f'Solving failed, cells left: {cells_left}')
        for i in range(1, 10):
            opposite_possible_values(i)
            print()

    print(grid)
    # print_possible_values()

    # for i in range(1, 10):
    #     opposite_possible_values(i)

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
                    # elif cell.value != 0:
                    #     pr(cell.value)
                    else:
                        pr(' ')
                pr('||' if j % 3 == 2 else '|')
            print('')
        print(('=' if i % 3 == 2 else '-') * (4 * 9 + 3))
    print('')


def opposite_possible_values(value):
    for i in range(9):
        for j in range(9):
            cell = grid[i][j]
            if value in cell.possible_values:
                pr(value)
            else:
                pr('.')
            if j == 2 or j == 5:
                pr('|')
        print('')
        if i == 2 or i == 5:
            print('-' * (3 * 3 + 2))


def get_subgrid(g, i, j):
    return g[i * 3:i * 3 + 3, j * 3:j * 3 + 3]


def solve_twos(i1):
    global grid
    grid2 = np.empty([9, 9], dtype=object)

    for i in range(9):
        for j in range(9):
            cell = grid[i][j]
            new_cell = Cell(i, j)
            new_cell.force_value(int(i1 in cell.possible_values))
            grid2[i][j] = new_cell


    # For all subgrids
    for i in range(3):
        for j in range(3):
            grid_9 = get_subgrid(grid2, i, j)
            subgrid = (i, j)
            surrounding_row = []
            surrounding_col = []
            for k in range(3):
                surrounding_row.append((i, k))
                surrounding_col.append((k, j))

            surrounding_row.remove(subgrid)
            surrounding_col.remove(subgrid)

            sums_total = [0, 0, 0]
            sums_partial1 = [0, 0, 0]
            sums_partial2 = [0, 0, 0]
            sg1 = get_subgrid(grid2, surrounding_row[0][0], surrounding_row[0][1])
            sg2 = get_subgrid(grid2, surrounding_row[1][0], surrounding_row[1][1])
            # print(sg1)
            # print(sg2)
            for x in range(3):
                for y in range(3):
                    sums_total[x] += sg1[x][y].value + sg2[x][y].value
                    sums_partial1[x] += sg1[x][y].value
                    sums_partial2[x] += sg2[x][y].value

            for r in range(3):
                others = [0, 1, 2]
                others.remove(r)
                if sums_total[r] == 0 and \
                        sums_partial1[others[0]] >= 1 and sums_partial1[others[1]] >= 1 and \
                        sums_partial2[others[0]] >= 1 and sums_partial2[others[1]] >= 1:
                    print('Number:', str(i1))
                    print(grid2)
                    print('Current subgrid:')
                    print(subgrid)
                    print(grid_9)
                    print('surrounding row subgrids:')
                    print(surrounding_row)
                    print(sums_total)
                    for c in range(3):
                        for o in others:
                            temp_cell: Cell = grid_9[o][c]
                            cell: Cell = grid[temp_cell.x][temp_cell.y]
                            if i1 in cell.possible_values:
                                print(f'Removing {i1} from ({cell.x}, {cell.y}) possible values')
                                # cell.possible_values.remove(i1)
                                cell.remove_possible_value(i1)


            sums_total = [0, 0, 0]
            sums_partial1 = [0, 0, 0]
            sums_partial2 = [0, 0, 0]
            sg1 = get_subgrid(grid2, surrounding_col[0][0], surrounding_col[0][1])
            sg2 = get_subgrid(grid2, surrounding_col[1][0], surrounding_col[1][1])
            # print(sg1)
            # print(sg2)
            for y in range(3):
                for x in range(3):
                    sums_total[y] += sg1[x][y].value + sg2[x][y].value
                    sums_partial1[y] += sg1[x][y].value
                    sums_partial2[y] += sg2[x][y].value

            for c in range(3):
                others = [0, 1, 2]
                others.remove(c)
                if sums_total[c] == 0 and \
                        sums_partial1[others[0]] >= 1 and sums_partial1[others[1]] >= 1 and \
                        sums_partial2[others[0]] >= 1 and sums_partial2[others[1]] >= 1:
                    print('Number:', str(i1))
                    print(grid2)
                    print('Current subgrid:')
                    print(subgrid)
                    print(grid_9)
                    print('surrounding col subgrids:')
                    print(surrounding_col)
                    print(sums_total)
                    for r in range(3):
                        for o in others:
                            temp_cell: Cell = grid_9[r][o]
                            cell: Cell = grid[temp_cell.x][temp_cell.y]
                            if i1 in cell.possible_values:
                                print(f'Removing {i1} from ({cell.x}, {cell.y}) possible values')
                                # cell.possible_values.remove(i1)
                                cell.remove_possible_value(i1)

    # for i in range(9):
    #     for j in range(9):
    #         cell: Cell = grid[i][j]
    #         # cell.update_surrounding()
    #         # cell.update_surrounding()
    print()


if __name__ == '__main__':
    app()
