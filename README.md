# Maze Traversal Project

This project is a Python implementation of a maze generator and solver using Depth-First Search (DFS), Breadth-First Search (BFS), and A* algorithms. The maze is generated using a binary tree algorithm, and the user can specify the size of the maze and the starting and ending points. The project is divided into two main files: `MazeGen.py` (maze generator) and `MazeGame.py` (maze solver).


## Introduction

The Maze Traversal Project is designed to demonstrate the use of different pathfinding algorithms to solve a maze. The maze is generated using a binary tree algorithm, which creates a grid of walls and paths. The user can specify the size of the maze and the starting and ending points. The project then uses DFS, BFS, and A* algorithms to find a path from the start to the end of the maze.

## Features

- **Maze Generation**: Generates a maze using a binary tree algorithm.
- **Pathfinding Algorithms**: Implements DFS, BFS, and A* algorithms to solve the maze.
- **Customizable Maze Size**: Allows the user to specify the size of the maze.
- **Interactive Start and End Points**: The user can specify the starting and ending points of the maze.
- **Visualization**: Displays the maze with the path found by the algorithm.

## Installation

To run this project, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/maze-traversal-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd maze-traversal-project
   ```
3. Install the required dependencies (if any):
   ```bash
   pip install numpy
   ```

## Usage

1. Run the `MazeGame.py` script:
   ```bash
   python MazeGame.py
   ```
2. Enter the size of the maze when prompted.
3. Enter the starting and ending coordinates when prompted.
4. The program will display the maze and the paths found using DFS, BFS, and A* algorithms.

## Algorithms

### DFS

Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root node and explores as far as possible along each branch before backtracking.

### BFS

Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root node and explores all the neighboring nodes at the present depth prior to moving on to nodes at the next depth level.

### A*

A* is a pathfinding algorithm that uses a heuristic to estimate the cost of the cheapest path from the start node to the goal node. It is more efficient than DFS and BFS for many problems because it uses a heuristic to guide its search.

## Maze Generation

The maze is generated using a binary tree algorithm. The algorithm works by carving out paths in a grid, where each cell can either be a wall or a path. The maze is represented as a 2D NumPy array, where walls are represented by `#` and paths are represented by spaces.

The maze generation process involves the following steps:
1. **Preprocessing**: The grid is preprocessed to ensure that the first row and last column are paths.
2. **Carving**: The grid is carved out to create paths based on a random binomial distribution.
3. **Output**: The final maze is output as a 2D array, with the starting and ending points marked by `S` and `E`, respectively.

---

If you have any questions or need further assistance, please don't hesitate to ask!
