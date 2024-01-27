# 8-Puzzle Solver

This Python program provides implementations of the Iterative Deepening Depth-First Search (IDDFS) and A* algorithms to solve the classic 8-puzzle problem. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with 8 numbered tiles and one empty space. The goal is to rearrange the tiles to reach a specified goal state.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## Introduction

The program includes two algorithms for solving the 8-puzzle problem:

1. **Iterative Deepening Depth-First Search (DFS):** Iterative Deepening Depth-First Search is used to explore the puzzle state space until a solution is found. The depth of the search is gradually increased until a solution is reached.

2. ***A* Algorithm:** A* search algorithm is employed, combining the depth of the search with a heuristic function to guide the exploration. The heuristic used is the count of misplaced tiles.

## Usage

To run the program, follow these steps:

1. Navigate to the game directory:
   ```bash
   cd C:\Users\Vijay\OneDrive\Documents\Artificial_Intelligence\Assignments\PuzzleGame Framework\game
   ```
2. Execute the puzzle.py file to start the game:
   ```bash
   python puzzle.py
   ```
3. Follow the instructions provided to enter the initial state of the puzzle. The program will output the final path to the solution.

## Algorithms

### Iterative Deepening Depth-First Search (IDDFS)

The IDDFS algorithm explores the puzzle state space in a depth-first manner, gradually increasing the depth of the search until a solution is found.

### A* Algorithm

The A* algorithm combines the depth of the search with a heuristic function to guide the exploration. The heuristic used is the count of misplaced tiles. The program employs priority queues to efficiently select nodes for expansion.


## File Structure

The project directory structure is organized as follows:

- `C:\Users\Vijay\OneDrive\Documents\Artificial_Intelligence\Assignments\PuzzleGame Framework\`
  - `game/`: Directory containing the files that build the game.
    - `puzzle.py`: Execute this file to start the game.
    - `...` (other game-related Python files)
  - `sol/`: Directory containing the solution file.
  - `README.md`: Documentation file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
