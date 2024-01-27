# This is the only file you need to work on. You do NOT need to modify other files

# Importing necessary modules
from game.Node import Node
import copy

# Define the goal state and possible moves for each puzzle position
solution = [0, 1, 2, 3, 4, 5, 6, 7, 8]
possibilities = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]

# Function to find child nodes of a given puzzle state
def find_children(puzzle):
    """Generate child nodes by exploring possible moves from the current puzzle state."""
    children = []
    empty_space_index = puzzle.puzzle.index(8)
    for i in possibilities[empty_space_index]:
        child = swap_values(puzzle.puzzle, i, empty_space_index)
        new_child_node = Node(parent=puzzle, puzzle=child, cost=puzzle.cost + 1)
        children.insert(0, new_child_node)
    return children

# Function to swap values in a puzzle state
def swap_values(puzzle, i1, i2):
    """Swap values in the puzzle to simulate a move."""
    temp_puzzle = copy.deepcopy(puzzle)
    temp_puzzle[i1], temp_puzzle[i2] = temp_puzzle[i2], temp_puzzle[i1]
    return temp_puzzle

# Depth-first search algorithm
def dfs(puzzle, cost):
    """Depth-First Search algorithm to find a solution."""
    root_node = Node(parent=None, puzzle=puzzle, cost=0)
    search_list = [root_node]
    visited_node = []
    while search_list:
        current_node = search_list.pop()
        if current_node.puzzle in search_list:
            continue
        if check_sol(current_node.puzzle):
            return current_node
        else:
            if current_node.cost < cost:
                children = find_children(current_node)
                search_list.extend(children)
        visited_node.append(current_node.puzzle)

    return None

# Function to find the path from the initial state to the final state
def find_path(final_node):
    """Backtrack to find the path from the final node to the root."""
    path = []
    while final_node.parent is not None:
        path.insert(0, final_node.puzzle.index(8))
        final_node = final_node.parent
    path.insert(0, final_node.puzzle.index(8))

    return path

# Iterative deepening algorithm
def iterativeDeepening(puzzle):
    """Iterative Deepening Depth-First Search algorithm."""
    cost = 0
    while True:
        result = dfs(puzzle, cost)
        if result is not None:
            path = find_path(result)
            print("Final Path = ", path)
            return path

        cost += 1

# Function to check if the puzzle state is the goal state
def check_sol(puzzle):
    """Check if the current puzzle state is the goal state."""
    return puzzle == solution

# A* algorithm
def astar(puzzle):
    """A* algorithm for solving the 8-puzzle problem."""
    open_list = []
    closed_set = set()

    root_node = Node(parent=None, puzzle=puzzle, cost=0)
    open_list.append(root_node)

    while open_list:
        open_list.sort(key=lambda x: x.cost + calculate_heuristic(x.puzzle))
        current_node = open_list.pop(0)
        
        if check_sol(current_node.puzzle):
            path = find_path(current_node)
            print("Final Path = ", path)
            return path

        closed_set.add(tuple(current_node.puzzle))

        children = find_children(current_node)
        for child in children:
            if tuple(child.puzzle) not in closed_set:
                child.cost = current_node.cost + 1 
                child.heuristic = calculate_heuristic(child.puzzle)

                open_list.append(child)
    return None  

# Heuristic function to calculate the number of misplaced tiles
def calculate_heuristic(puzzle):
    """Calculate the heuristic value for the A* algorithm."""
    return sum([1 if puzzle[i] != solution[i] else 0 for i in range(len(puzzle))])