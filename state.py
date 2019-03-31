import sys
import copy 
import numpy as np

# Class that represents a state in the game's decision tree
# A state is, in practice, a possible board configuration
class State:
    # Initializer method
    def __init__(self, size, current_state, father_state = None, blank_x = None, blank_y = None):
        self.size = size
        self.current_state = current_state
        self.father_state = father_state
        self.upper_child = None
        self.lower_child = None
        self.left_child  = None
        self.right_child = None
        if father_state is None:
            self.current_level = 0
        else:
            self.current_level = father_state.current_level + 1
        if blank_x is None or blank_y is None:
            blank_position = np.where(current_state == 0)
            self.blank_y = blank_position[0][0]
            self.blank_x = blank_position[1][0]
        else:
            self.blank_x = blank_x
            self.blank_y = blank_y

    # ----------------------- Up state methods ---------------------------

    # Method that represents the board state after moving a piece upwards
    # If the moviment is impossible, this method will return None
    def up_state(self):
        # If the upper child have already been generated, returns it
        if self.upper_child is not None:
            return self.upper_child
        # If the upper child is None, generate it, store it, and return it
        else:
            self.upper_child = self.generate_up_state()
            return self.upper_child

    # Method that generates the up state, if an upwards movement is possible
    def generate_up_state(self):
        # Return None if the movement is impossible
        if (self.blank_y + 1) == self.size:
            return None
        # If the movement is possible, make it and return the new state
        new_state = self.move_up()
        return State(new_state, self.size, self, self.blank_x, self.blank_y + 1)

    # Method that that moves a piece upwards
    def move_up(self):
        # Copy the current state matrix and them change its values
        new_state = copy.deepcopy(self.current_state)
        new_state[self.blank_y][self.blank_x] = new_state[self.blank_y + 1][self.blank_x]
        new_state[self.blank_y + 1][self.blank_x] = 0
        return new_state

    # ----------------------- Down state methods ---------------------------

    # Method that represents the board state after moving a piece downwards
    # If the moviment is impossible, this method will return None
    def down_state(self):
        # If the lower child have already been generated, returns it
        if self.lower_child is not None:
            return self.lower_child
        # If the lower child is None, generate it, store it, and return it
        else:
            self.lower_child = self.generate_down_state()
            return self.lower_child

    # Method that generates the down state, if a downwards movement is possible
    def generate_down_state(self):
        # Return None if the movement is impossible
        if (self.blank_y - 1) < 0:
            return None
        # If the movement is possible, make it and return the new state
        new_state = self.move_down()
        return State(new_state, self.size, self, self.blank_x, self.blank_y - 1)

    # Method that that moves a piece downwards
    def move_down(self):
        # Copy the current state matrix and them change its values
        new_state = copy.deepcopy(self.current_state)
        new_state[self.blank_y][self.blank_x] = new_state[self.blank_y - 1][self.blank_x]
        new_state[self.blank_y - 1][self.blank_x] = 0
        return new_state

    # ----------------------- Left state methods ---------------------------

    # Method that represents the board state after moving a piece to the left
    # If the moviment is impossible, this method will return None
    def left_state(self):
        # If the left child have already been generated, returns it
        if self.left_child is not None:
            return self.left_child
        # If the left child is None, generate it, store it, and return it
        else:
            self.left_child = self.generate_left_state()
            return self.left_child

    # Method that generates the left state, if a left movement is possible
    def generate_left_state(self):
        # Return None if the movement is impossible
        if (self.blank_x + 1) == self.size:
            return None
        # If the movement is possible, make it and return the new state
        new_state = self.move_left()
        return State(new_state, self.size, self, self.blank_x + 1, self.blank_y)

    # Method that that moves a piece left
    def move_left(self):
        # Copy the current state matrix and them change its values
        new_state = copy.deepcopy(self.current_state)
        new_state[self.blank_y][self.blank_x] = new_state[self.blank_y][self.blank_x + 1]
        new_state[self.blank_y][self.blank_x + 1] = 0
        return new_state

    # ----------------------- Right state methods ---------------------------

    # Method that represents the board state after moving a piece to the right
    # If the moviment is impossible, this method will return None
    def right_state(self):
        # If the upper child have already been generated, returns it
        if self.right_child is not None:
            return self.right_child
        # If the upper child is None, generate it, store it, and return it
        else:
            self.right_child = self.generate_right_state()
            return self.right_child

    # Method that generates the right state, if a right movement is possible
    def generate_right_state(self):
        # Return None if the movement is impossible
        if (self.blank_x - 1) < 0:
            return None
        # If the movement is possible, make it and return the new state
        new_state = self.move_right()
        return State(new_state, self.size, self, self.blank_x - 1, self.blank_y)

    # Method that that moves a piece right
    def move_right(self):
        print(self.current_state)
        # Copy the current state matrix and them change its values
        new_state = copy.deepcopy(self.current_state)
        new_state[self.blank_y][self.blank_x] = new_state[self.blank_y][self.blank_x - 1]
        new_state[self.blank_y][self.blank_x - 1] = 0
        print(new_state)
        return new_state

   # ------------------- Getters ----------------------------------------
    def get_current_state(self):
       return self.current_state

    def get_blank_x(self):
        return self.blank_x

    def get_blank_y(self):
        return self.blank_y

    def get_father_state(self):
        return self.father_state

    def get_current_level(self):
        return self.current_level

    
        
