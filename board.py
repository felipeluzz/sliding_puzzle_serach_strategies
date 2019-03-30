import sys
import itertools
import numpy as np

# Class that represents the sliding puzzle board
class Board:
    # Initializer method
    def __init__(self, size):
        self.size = size
        self.board = self.random_board()
        print(self.board)

    # Generate victory state
    def winning_board(self):
        board = np.arange(1, self.size*self.size+1).reshape(self.size, self.size)
        board[-1][-1] = 0
        return board

    # Generate random board
    def random_board(self):
        while True:
            board = self.winning_board()
            np.random.shuffle(board)
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

    # Check if the blank is in and even row
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
        

# TEST
if len(sys.argv) > 1:
    board = Board(int(sys.argv[1]))
else:
    sys.exit("Missing parameter: board size") 

