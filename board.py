import sys
import state
import numpy as np

# Class that represents the sliding puzzle board
class Board:
    # Initializer method
    def __init__(self, size):
        self.size = size
        self.board = self.random_board()
        # Test board below
        # self.board = np.array([[7,1,2], [4,6,5], [3,8,0]])
        self.initial_state = state.State(self.size, self.board)

    # Generate victory state
    def winning_board(self):
        board = np.arange(1, self.size*self.size+1).reshape(self.size, self.size)
        board[-1][-1] = 0
        return board

    # Generate random board
    def random_board(self):
        while True:
            board = self.winning_board().flatten()
            np.random.shuffle(board)
            board = board.reshape(self.size, self.size)
            if self.solvable(board):
                break
        return board

    # Check if board is solvable
    def solvable(self, board):
        flat_board = board.flatten()
        # Case where the size of the board is odd
        if (self.size % 2) != 0:
            if (self.invertion_count(flat_board) % 2) == 0:
                return True
        # Case where the size of the board is even
        else:
            if ((self.invertion_count(flat_board) % 2) == 0) and (not self.even_blank_position(board)):
                return True
            if ((self.invertion_count(flat_board) % 2) != 0) and (self.even_blank_position(board)):
                return True
        return False

    # Get the number of inversions of the current board
    def invertion_count(self, board):
        n = len(board) 
        invertion_count = 0
        for i in range(n): 
            for j in range(i + 1, n): 
                if (board[i] > board[j]): 
                    invertion_count += 1
        return invertion_count 

    # Check if the blank is in and even row, counting from the bottom
    def even_blank_position(self, board):
        position = self.size - np.where(board == 0)[0] 
        if (position % 2) == 0:
            return True
        else:
            return False

    # Get board size
    def get_size(self):
        return self.size

    # Get board
    def get_board(self):
        return self.board

    # Set board
    def set_board(self, board):
        self.board = board

    # Get initial state
    def get_initial_state(self):
        return self.initial_state
        



