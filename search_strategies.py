import sys
import board
import numpy as np
import time

# Main search method, that will call the method of the search strategy
# passed by command line argument. The limit parameter is used only for the
# iterative deepening depth-first strategy.
def search(board, strategy, h = None):
    if strategy == 'breadth':
        final_state = breadth_first_strategy(board)
    elif strategy == 'depth':
        final_state = depth_first_strategy(board)
    elif strategy == 'iterative':
        final_state = iterative_depth_first_strategy(board, 5)
    elif strategy == 'A*':
        final_state = astar_strategy(board, h)
    else:
        print('Unknown strategy')
        exit()

    if final_state is None:
        print("No solution found")
        exit()
    else:
        print("Final State: ")
        print(final_state.get_current_state())
        solution_moviments = solution(final_state)
        print("Solution: ")
        print(solution_moviments)

# --------------------- Breadth-first strategy ------------------------------
# Method that implements the Breadth-first search strategy, recives the 
# initial board as a parameter.
def breadth_first_strategy(board):
    # Initialize the list of states and put the root state in it
    states = []
    states.append(board.get_initial_state())

    # Count the number of visited states
    visited_states = 0

    print("Initial Board")
    print(board.get_initial_state().get_current_state())

    # Loop while the solution has not been found and the state list is not empty
    while True:

        # Get the current state
        current_state = states.pop(0)

        print("Visited States: " + str(visited_states))
        print("Current Queue Size: " + str(len(states)))
        print("Current Level: " + str(current_state.get_current_level()))

        # Check if the current state is the winning state, returns it if it is
        if np.array_equal(board.winning_board(), current_state.get_current_state()):
            return current_state 

        # Put the children of the current state in the states list
        states += current_state.get_children()

        # Ends loop if the states list is empty
        if len(states) <= 0:
            break 

        # Increment visited states counter
        visited_states += 1
    
    # If no solution could be found, return None
    return None

# --------------------- Depth-first strategy ------------------------------
# Method that implements the Depth-first search strategy, recives the 
# initial board as a parameter.
def depth_first_strategy(board):
    # Initialize the list of states and put the root state in it
    states = []
    states.append(board.get_initial_state())

    # Count the number of visited states
    visited_states = 0

    print("Initial Board")
    print(board.get_initial_state().get_current_state())

    # Loop while the solution has not been found and the state list is not empty
    while True:

        # Get the current state
        current_state = states.pop()

        print("Visited States: " + str(visited_states))
        print("Current Queue Size: " + str(len(states)))
        print("Current Level: " + str(current_state.get_current_level()))

        # Check if the current state is the winning state, returns it if it is
        if np.array_equal(board.winning_board(), current_state.get_current_state()):
            return current_state 

        # Put the children of the current state in the states list
        states += current_state.get_children()

        # Ends loop if the states list is empty
        if len(states) <= 0:
            break 

        # Increment visited states counter
        visited_states += 1
    
    # If no solution could be found, return None
    return None

# --------------------- Iterative Depth-first strategy -------------------------
# Method that implements the Iterative Depth-first search strategy, recives the 
# initial board and the increment as parameters.
def iterative_depth_first_strategy(board, increment):

    # Count the number of visited states
    visited_states = 0

    print("Initial Board")
    print(board.get_initial_state().get_current_state())

    # Max depth of the search
    max_depth = 0

    iteration = 0

    while True:

        iteration += 1
        print("Iteration: " + str(iteration))

        # Increment the max depth
        max_depth += increment

        # Initialize the list of states and put the root state in it
        states = []
        states.append(board.get_initial_state())

        print("Max Depth: " + str(max_depth))


        # Loop while the solution has not been found and the state list is not empty
        while True:

            # Get the current state
            current_state = states.pop()

            print("Visited States: " + str(visited_states))
            print("Current Queue Size: " + str(len(states)))
            print("Current Level: " + str(current_state.get_current_level()))

            # Check if the current state is the winning state, returns it if it is
            if np.array_equal(board.winning_board(), current_state.get_current_state()):
                return current_state 

            # Put the children of the current state in the states list, but only
            # if the current level is not higher than the max depth
            if (current_state.get_current_level()) <= max_depth:
                states += current_state.get_children()

            # Ends loop if the states list is empty
            if len(states) <= 0:
                break 

            # Increment visited states counter
            visited_states += 1

        # If depth 30 is reached with no solution, end the search and return None
        if max_depth > 30:
            break
    
    # If no solution could be found, return None
    return None

# --------------------- A* strategy ------------------------------
from heapq import heappush, heappop

def heuristic(h, current, final):
    count = 0
    for i in range(0, len(current)):
        for j in range(0, len(current)):
            if h != 'manhattan':
                if current[i][j] != final[i][j] and current[i][j] != 0:
                    count += 1
            else:
                count += abs(current[i][j] // 3 - final[i][j] // 3) + abs(current[i][j] % 3 - final[i][j] % 3)
    return count

# Method that implements the Breadth-first search strategy, recives the 
# initial board as a parameter.
def astar_strategy(board, h):
    # Initialize the list of states and put the root state in it
    states = []  
    #states.append(board.get_initial_state())
    
    # Push root node to queue
    cost = heuristic(h, board.get_initial_state().get_current_state(), board.winning_board()) + board.get_initial_state().get_current_level()
    item = (cost, board.get_initial_state())
    heappush(states, item)

    # Initialize visted states array
    visited = []
    visited_states = 0

    print("Initial Board")
    print(board.get_initial_state().get_current_state())

    # Loop while the solution has not been found and the state list is not empty
    while True:

        # Get the first state from queue
        current_state = heappop(states)[1]
        
        print("Visited States: " + str(visited_states))
        print("Current Queue Size: " + str(len(states)))
        print("Current Level: " + str(current_state.get_current_level()))
        
        # Check if the current state is the winning state, returns it if it is
        if np.array_equal(board.winning_board(), current_state.get_current_state()):
            return current_state 

        # Add current state to visited list
        visited.append(current_state.get_current_state())
        
        # Put the children of the current state in the states liststates += 
        for child in current_state.get_children():
            # Push root node to queue
            cost = heuristic(h, child.get_current_state(), board.winning_board()) + child.get_current_level()
            item = (cost, child)
            heappush(states, item)
                
        # Ends loop if the states list is empty
        if len(states) <= 0:
            break 

        # Increment visited states counter
        visited_states += 1
    
    # If no solution could be found, return None
    return None


# ------------------------------- Puzzle solution ------------------------------

# Method that traces back the moviments from a given final state to the initial state
def solution(final_state):
    moves = []
    father_state = final_state

    # Loops unitl the initial state is reached
    while True:
        current_state = father_state
        father_state = father_state.get_father_state()

        # If there is no father, the initial state has been reached
        if father_state is None:
            break
        
        # Add to the start of the list the movement from the father state necessary
        # to reach the current state
        up_state = father_state.up_state()
        if not up_state is None:
            if np.array_equal(up_state.get_current_state(), current_state.get_current_state()):
                moves.insert(0, 'UP')
        down_state = father_state.down_state()
        if not down_state is None:
            if np.array_equal(down_state.get_current_state(), current_state.get_current_state()):
                moves.insert(0, 'DOWN')  
        left_state = father_state.left_state()
        if not left_state is None:
            if np.array_equal(left_state.get_current_state(), current_state.get_current_state()):
                moves.insert(0, 'LEFT')  
        right_state = father_state.right_state()
        if not right_state is None:
            if np.array_equal(right_state.get_current_state(), current_state.get_current_state()):
                moves.insert(0, 'RIGHT') 

    return moves

# TEST
if len(sys.argv) > 3:
    board = board.Board(int(sys.argv[1]))
    search(board, sys.argv[2], sys.argv[3])
elif len(sys.argv) > 2:
    board = board.Board(int(sys.argv[1]))
    search(board, sys.argv[2])
else:
    sys.exit("Arguments needed: board size, search strategy (breadth, depth, iterative, A*)\n If you want to use the manhattan distance in the A* strategy, type manhattan as the last argument ") 