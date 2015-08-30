"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you may ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """Simple class that implements Solitaire Mancala"""
    
    def __init__(self):
        """Create Mancala game with empty store and no houses"""
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = list(configuration)
    
    def __str__(self):
        """Return string representation for Mancala board"""
        return str(self._board[::-1])
    
    def get_num_seeds(self, house_num):
        """Return the number of seeds in given house on board"""
        return self._board[house_num]

    def is_game_won(self):
        """Check to see if all houses but house zero are empty"""
        if sum(self._board[1:]) == 0:
            return True
        else:
            return False
    
    def is_legal_move(self, house_num):
        """Check whether a given move is legal"""
        if (house_num != 0) and (self._board[house_num] == house_num):
            return True
        else:
            return False
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            self._board[house_num] = 0
            for idx in range(house_num):
                self._board[idx] += 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for idx in range(len(self._board)):
            if self.is_legal_move(idx):
                return idx
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        _cache = list(self._board)
        moves = []
        while self.choose_move():
            house = self.choose_move()
            moves.append(house)
            self.apply_move(house)

        self._board = list(_cache)
        return moves
 

# Create tests to check the correctness of your code

def test_mancala():
    """Test code for Solitaire Mancala"""
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(config1)
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
    print

    # add more tests here
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False
    my_game.set_board([5, 0, 0, 0, 0, 0, 0]) 
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", True
    my_game.set_board(config1)
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False
    print

    print "Testing is_legal_move - Computed:", 
    for i in range(7):
        print my_game.is_legal_move(i),
    print "Expected:", False, False, False, False, False, True, False

    my_game.set_board([2, 0, 2, 1, 4, 5, 0])
    print "Testing is_legal_move - Computed:", 
    for i in range(7):
        print my_game.is_legal_move(i),
    print "Expected:", False, False, True, False, True, True, False
    print


    my_game.set_board(config1)
    print "Testing apply_move - Computed:", 
    my_game.apply_move(5)
    print str(my_game), "Expected:", str([0, 0, 4, 2, 2, 1, 1])

    print "Testing apply_move - Computed:", 
    my_game.apply_move(5)
    print str(my_game), "Expected:", str([0, 0, 4, 2, 2, 1, 1])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    print "Testing apply_move - Computed:", 
    my_game.apply_move(1)
    print str(my_game), "Expected:", str([0, 0, 4, 2, 2, 0, 2])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 2
    print "Testing apply_move - Computed:", 
    my_game.apply_move(2)
    print str(my_game), "Expected:", str([0, 0, 4, 2, 0, 1, 3])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    print "Testing apply_move - Computed:", 
    my_game.apply_move(1)
    print str(my_game), "Expected:", str([0, 0, 4, 2, 0, 0, 4])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 4
    print "Testing apply_move - Computed:", 
    my_game.apply_move(4)
    print str(my_game), "Expected:", str([0, 0, 0, 3, 1, 1, 5])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    print "Testing apply_move - Computed:", 
    my_game.apply_move(1)
    print str(my_game), "Expected:", str([0, 0, 0, 3, 1, 0, 6])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 3
    print "Testing apply_move - Computed:", 
    my_game.apply_move(3)
    print str(my_game), "Expected:", str([0, 0, 0, 0, 2, 1, 7])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    print "Testing apply_move - Computed:", 
    my_game.apply_move(1)
    print str(my_game), "Expected:", str([0, 0, 0, 0, 2, 0, 8])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 2
    print "Testing apply_move - Computed:", 
    my_game.apply_move(2)
    print str(my_game), "Expected:", str([0, 0, 0, 0, 0, 1, 9])

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    print "Testing apply_move - Computed:", 
    my_game.apply_move(1)
    print str(my_game), "Expected:", str([0, 0, 0, 0, 0, 0, 10])
    print

    my_game.set_board(config1)
    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", [5, 1, 2, 1, 4, 1, 3, 1, 2, 1]
    my_game.set_board([4, 0, 3, 1, 2, 3, 4])
    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", []
    my_game.set_board([2, 0, 2, 2, 4, 5, 7])
    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", [2, 1, 4, 1, 3, 1, 2, 1, 5, 1]
    print

    # print "Testing apply_move - Computed:"
    # plan = my_game.plan_moves()
    # for mv in plan:
    #     print mv, str(my_game)
    #     my_game.apply_move(mv)
    # print my_game


test_mancala()


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
