from math import dist
from MazeGen import Maze


class MazeGame:
    def __init__(self, size):
        self.maze_obj = Maze(size)
        self.maze_array = self.maze_obj.maze_ndarray
        # self.maze_obj.print()  # UNCOMMENT

        for row in range(self.maze_obj.size):
            for col in range(self.maze_obj.size):
                print(self.maze_array[row][col], end=" ")
            print(row + 1)

        for i in range(self.maze_obj.size):
            print((i + 1) // 10 if (i + 1) > 9 else i + 1, end=" ")
        print()
        for i in range(self.maze_obj.size):
            print((i + 1) % 10 if (i + 1) > 9 else " ", end=" ")
        print()

        self.__postInit()

    def __postInit(self):
        start_end_coords = []

        for i in range(4):
            row_or_col = "row" if i % 2 == 0 else "col"
            start_or_end = "start" if i < 2 else "end"
            input_num = input(f"\ninsert {row_or_col} no. for {start_or_end}: ")
            while not input_num.isnumeric():
                print("please enter a number")
                input_num = input(f"insert {row_or_col} no. for {start_or_end}: ")
            start_end_coords.append(int(input_num) - 1)

        self.maze_obj.setStartAndEnd(*start_end_coords)
        self.maze_obj.print()

    def __isValidMove(self, r, c):
        return (0 <= r < self.maze_obj.size) and (0 <= c < self.maze_obj.size) and (
                self.maze_array[r][c] in [' ', 'E'])

    def bfs(self):
        from collections import deque

        visited = set()
        queue = deque([(self.maze_obj.start_coord, [])])

        while queue:
            cur_coord, cur_path = queue.popleft()

            if cur_coord == self.maze_obj.end_coord:
                return cur_path, visited

            for row_movement, col_movement in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_coord = (cur_coord[0] + row_movement, cur_coord[1] + col_movement)

                if self.__isValidMove(*new_coord) and (new_coord not in visited):
                    queue.append((new_coord, cur_path + [cur_coord]))
                    visited.add(cur_coord)
        return None, visited

    def dfs(self):
        stack: list[tuple[tuple, list[tuple[int, int]]]] = [(self.maze_obj.start_coord, [])]
        visited = set()
        visited.add(self.maze_obj.start_coord)
        while stack:
            cur_coord, cur_path = stack.pop()

            if cur_coord == self.maze_obj.end_coord:
                return cur_path, visited

            for row_mvmt, col_mvmt in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_coord = (cur_coord[0] + row_mvmt, cur_coord[1] + col_mvmt)

                if self.__isValidMove(*new_coord) and (new_coord not in visited):
                    stack.append((new_coord, cur_path + [cur_coord]))
                    visited.add(cur_coord)

        return None, visited

    def aStar(self):
        """
        A Star searching algorthm using euclidian distance as heuristic value. \n
        g cost = distance from start to current position \n
        h cost = distance from current position to end \n
        f cost = g cost + h cost \n
        in case no path found from start to end, returns (None, all visited paths)
        :return: Tuple(path from start to end, all the paths visited)
        """

        open_list: list = []  # Open List to keep track of the tiles possible to explore further
        visited = set()  # Visited Set to keep track of tiles whose neighbours have been explored
        start = self.maze_obj.start_coord  # Coordinates of the Starting tile
        end = self.maze_obj.end_coord  # Coordinates of the Ending tile

        open_list.append(([*start, 0, 0], []))

        # open_list entry is a Tuple of 2 values - List[row, col, gCost, hCost] and PATH List of Tuples of (row, col)
        # gCost is the distance from start, hCost is the distance from end

        def fCost(open_list_entry):
            g_cost = open_list_entry[0][2]
            h_cost = open_list_entry[0][3]
            return round(g_cost + h_cost, 2)

        def g_hCost(row_col_coord: list):
            # Euclidean Distance between 2 points calculated using math.dist
            # Distance between x and y = sqrt((x2 - x1)**2 + (y2 - y1)**2)
            g_cost = round(dist(row_col_coord, start), 2)
            h_cost = round(dist(row_col_coord, end), 2)
            return g_cost, h_cost

        while open_list:
            min_f_cost_entry = open_list[0]  # explore the tile with lowest fCost in every iteration
            for entry in open_list:  # Loop to search for the tile with Lowest fCost and in case of 2 tiles with same fCost - tile with lower hCost is selected
                if (fCost(entry) < fCost(min_f_cost_entry)) or (entry[0][3] < min_f_cost_entry[0][3]):
                    min_f_cost_entry = entry
            cur_coord, cur_path = min_f_cost_entry
            open_list.remove(min_f_cost_entry)  # Removing the tile being explored from the open list
            visited.add((cur_coord[0], cur_coord[1]))  # Adding the tile being explored to the visited set

            if cur_coord[0] == end[0] and cur_coord[1] == end[1]:  # if the current tile and the end tile have same coordinates
                return cur_path, visited

            for row_mvmt, col_mvmt in [(-1, 0), (1, 0), (0, -1),
                                       (0, 1)]:  # Explore each neighbour top, bottom, left, right
                neighbour_coord = [cur_coord[0] + row_mvmt, cur_coord[1] + col_mvmt]

                if self.__isValidMove(*neighbour_coord) and (
                        tuple(
                            neighbour_coord) not in visited):  # if neighbour is not a wall and neighbour is not already explored
                    neighbour_coord.extend(
                        [*g_hCost(neighbour_coord)])  # calculate new gCost and hCost for the neighbour

                    neighbour_coord_found = False
                    for entry in open_list:  # See if the neighbour is already in the open_list
                        coord = entry[0]
                        if coord[0] == neighbour_coord[0] and coord[1] == neighbour_coord[1]:  # if neighbour is present in the open_list
                            if neighbour_coord[2] < coord[2]:  # If neighbour's new gCost is lesser than prev gCost, update the gCost and hCost for the neighbour in the open_list
                                coord[2], coord[3] = neighbour_coord[2], neighbour_coord[3]
                            neighbour_coord_found = True
                            break

                    if not neighbour_coord_found:  # if neighbour not already in the open_list, add it to the list along with the path to the neighbour
                        open_list.append([neighbour_coord, cur_path + [(cur_coord[0], cur_coord[1])]])

        return None, visited

    def print_path(self, sol_path: list, visited: list) -> None:
        """
        Only for Displaying Maze with paths, doesn't modify the maze_obj
        :param sol_path: path from start to end point
        :param visited: all the paths explored by the algorithm
        :return: None
        """
        maze_copy = self.maze_array.copy()
        for r, c in visited:
            if maze_copy[r][c] not in ['S', 'E']:
                maze_copy[r][c] = '*' if ((r, c) in sol_path) else "."

        for row in maze_copy:
            print(" ".join(row))
        print()


if __name__ == "__main__":
    maze_size = int(input('size: '))  # UNCOMMENT
    maze_game = MazeGame(maze_size)

    bfs_path, bfs_visited = maze_game.bfs()
    if bfs_path:
        print("Maze solved using BFS:")
        maze_game.print_path(bfs_path, bfs_visited)
    else:
        print("No solution found using BFS.")

    dfs_path, dfs_visited = maze_game.dfs()
    if dfs_path:
        print("Maze solved using DFS:")
        maze_game.print_path(dfs_path, dfs_visited)
    else:
        print("No solution found using DFS.")

    a_star_path, a_star_visited = maze_game.aStar()
    if a_star_path:
        print("Maze solved using A Star:")
        maze_game.print_path(a_star_path, a_star_visited)
    else:
        print("No solution found using A Star.")
