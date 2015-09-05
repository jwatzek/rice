"""
Clone of 2048 game.
"""

# import poc_2048_gui
import mini_project2_test as test
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

# Helper functions for merge
def slide(line):
    """
    Slide all non-zero values to the front of the list (lower indices). Returns
    list of same length.
    """
    result = [0] * len(line)
    idx = 0
    for entry in line:
        if entry != 0:
            result[idx] = entry
            idx += 1
    return result

def pair(line):
    """
    Pair adjacent tiles of the same value. Returns list of same length with 
    one tile of twice the value and a zero tile.
    """
    result = list(line)
    prev_merged = False

    for idx in range(len(line) - 1):
        if not prev_merged and line[idx] == line[idx + 1]:
            result[idx] *= 2
            result[idx + 1] *= 0
            prev_merged = True
        else:
            prev_merged = False

    return result

def merge(line):
    """Merges a single row or column in 2048."""
    slid = slide(line)
    paired = pair(slid)
    return slide(paired)


class TwentyFortyEight:
    """Class to run the game logic."""

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.reset()

    def reset(self):
        """Reset the game so the grid is empty except for two initial tiles."""
        self.board = [[0 for dummy_col in range(self.width)]
                         for dummy_row in range(self.height)]

        self.initial = {}
        self.initial[UP] = [(0, col) for col in range(self.width)]
        self.initial[DOWN] = [(self.height - 1, col) for col in range(self.width)]
        self.initial[LEFT] = [(row, 0) for row in range(self.height)]
        self.initial[RIGHT] = [(row, self.width - 1) for row in range(self.height)]

        # self.new_tile()
        # self.new_tile()
        return self.board

    def __str__(self):
        """Return a string representation of the grid for debugging."""
        prt = '\n'
        for row in self.board:
            prt += str(row) + '\n'

        return prt

    def get_grid_height(self):
        """Get the height of the board."""
        return self.height

    def get_grid_width(self):
        """Get the width of the board."""
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty = []
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == 0:
                    empty.append([row, col])

        if empty != []:
            idx = random.randrange(len(empty))
            num = random.random()
            if num < .9:
                self.set_tile(empty[idx][0], empty[idx][1], 2)
            else:
                self.set_tile(empty[idx][0], empty[idx][1], 4)

    def set_tile(self, row, col, value):
        """Set the tile at position row, col to have the given value."""
        if row < self.height and col < self.width:
            self.board[row][col] = value

    def get_tile(self, row, col):
        """Return the value of the tile at position row, col."""
        if row < self.height and col < self.width:        
            return self.board[row][col]

game = TwentyFortyEight(5, 4)
test.run_suite(game)
# poc_2048_gui.run_gui(TwentyFortyEight(4, 5))
