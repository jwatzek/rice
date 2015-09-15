"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 300       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):
    """
    Make random moves, alternating between players. Return when game is over. 
    Modify board input containing state of the game; no return value.
    """
    while board.check_win() == None:
        empty = board.get_empty_squares()
        idx = random.choice(empty)
        board.move(idx[0], idx[1], player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    """
    Score completed board and update scores grid directly; no return value.
    """
    dim = board.get_dim()
    opponent = provided.switch_player(player)

    if board.check_win() == player:
        for row in range(dim):
            for col in range(dim):
                if board.square(row, col) == player:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) == opponent:
                    scores[row][col] -= SCORE_OTHER

    elif board.check_win() == opponent:
        for row in range(dim):
            for col in range(dim):
                if board.square(row, col) == player:
                    scores[row][col] -= SCORE_CURRENT
                elif board.square(row, col) == opponent:
                    scores[row][col] += SCORE_OTHER

def get_best_move(board, scores):
    """
    Find all empty squares with maximum score and randomly return one of them as 
    (row, col) tuple. Do whatever if board is full.
    """
    best = []

    empty = board.get_empty_squares()
    subset = [scores[row][col] for row, col in empty]

    for (row, col) in empty:
        if scores[row][col] == max(subset):
            best.append((row, col))
    return random.choice(best)

def mc_move(board, player, trials):
    """
    Use Monte Carlo simulation to return a move for machine player as (row, col)
    tuple.
    """
    dim = board.get_dim()
    scores = [[0 for dummy_col in range(dim)]
                 for dummy_row in range(dim)]

    for dummy in range(trials):
        mcboard = board.clone()
        mc_trial(mcboard, player)
        mc_update_scores(scores, mcboard, player)

    return get_best_move(board, scores)



# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
