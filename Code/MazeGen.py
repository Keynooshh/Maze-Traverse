import numpy as np

# This algorithm uses binary tree as the solution
# Each node contains of the vertical or horizontal Path and wall
# Per number in preprocessed grid there will be a node
# Per node there will be 3 outputs carved in output grid
# Nodes can be: 1 -> it goes downwards  , 0 -> goes forward (To the right)
# Just like that we have paths carved through the grid
# Anything that isn't a path is a wall
# At the end we will declare the starting and ending point declared by the user

# class MazeTile:
#     def __init__(self, row: int, col: int, g_cost=0, h_cost=0, char="#"):
#         self.row = row
#         self.col = col
#         self.g_cost = g_cost
#         self.h_cost = h_cost
#         self.char = char
#
#     def coord(self) -> tuple[int, int]:
#         return self.row, self.col
#
#     def fCost(self) -> int:
#         return self.g_cost + self.h_cost


class Maze:
    def __init__(self, size) -> None:
        self.grid_size = size
        self.size = size * 3
        self.maze_ndarray = self.__getMazeNDArray()
        self.start_coord = (0, 0)
        self.end_coord = (0, 0)

    def __carveMaze(self, grid: np.ndarray) -> np.ndarray:
        output_grid = np.empty([self.size, self.size], dtype=str)
        output_grid[:] = '#'
        r = 0
        c = 0
        while r < self.grid_size:
            w = r * 3 + 1
            while c < self.grid_size:
                k = c * 3 + 1
                toss = grid[r, c]
                output_grid[w, k] = ' '
                output_grid[w, k] = ' '
                if toss == 0 and k + 2 < self.size:
                    output_grid[w, k + 1] = ' '
                    output_grid[w, k + 2] = ' '
                if toss == 1 and w - 2 >= 0:
                    output_grid[w - 1, k] = ' '
                    output_grid[w - 2, k] = ' '

                c = c + 1

            r = r + 1
            c = 0

        return output_grid

    def __preprocessGrid(self, grid: np.ndarray) -> np.ndarray:
        first_row = grid[0]
        first_row[first_row == 1] = 0
        grid[0] = first_row
        for i in range(1, self.grid_size):
            grid[i, self.grid_size - 1] = 1
        return grid

    def __getMazeNDArray(self) -> np.ndarray:
        n = 1
        p = 0.5
        np.random.seed(32)
        grid = np.random.binomial(n, p, size=(self.grid_size, self.grid_size))
        processed_grid = self.__preprocessGrid(grid)

        output = self.__carveMaze(processed_grid)

        return output

    def setStartAndEnd(self, start_row, start_col, end_row, end_col):
        self.start_coord = (start_row, start_col)
        self.end_coord = (end_row, end_col)
        self.maze_ndarray[start_row][start_col] = "S"
        self.maze_ndarray[end_row][end_col] = "E"

    def print(self):
        for row in self.maze_ndarray:
            print(" ".join(row))
        print()
