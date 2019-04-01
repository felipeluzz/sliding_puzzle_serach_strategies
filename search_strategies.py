import sys
import board
import numpy as np

# Main search method, that will call the method of the search strategy
# passed by command line argument. The limit parameter is used only for the
# iterative deepening depth-first strategy.
def search(board, strategy, increment = 5):
    if strategy == 'breadth':
        final_state = breadth_first_strategy(board)
    elif strategy == 'depth':
        final_state = depth_first_strategy(board)
    elif strategy == 'iterative':
        final_state = iterative_depth_first_strategy(board, increment)
    elif strategy == 'A*':
        final_state = 4
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
            if (current_state.get_current_level()) < max_depth:
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
        if np.array_equal(father_state.up_state().get_current_state(), current_state.get_current_state()):
            moves.insert(0, 'UP') 
        elif np.array_equal(father_state.down_state().get_current_state(), current_state.get_current_state()):
            moves.insert(0, 'DOWN')  
        elif np.array_equal(father_state.left_state().get_current_state(), current_state.get_current_state()):
            moves.insert(0, 'LEFT')  
        else:
            moves.insert(0, 'RIGHT') 

    return moves

# TEST
if len(sys.argv) > 2:
    board = board.Board(int(sys.argv[1]))
    search(board, sys.argv[2])
else:
    sys.exit("Arguments needed: board size, search strategy (breadth, depth, iterative, A*)") 