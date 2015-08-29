# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# define event handlers for control panel
def range100():
    """ Restarts game with secret number in range [0, 100). """
    global num_range, max_guesses
    num_range = 100
    max_guesses = 7
    new_game()
    
def range1000():
    """ Restarts game with secret number in range [0, 1000). """
    global num_range, max_guesses
    num_range = 1000
    max_guesses = 10
    new_game()
    
# helper function to start and restart the game
def new_game():
    global secret_number, num_guesses
    num_guesses = max_guesses
    secret_number = random.randrange(num_range)
    print
    print 'New game. Range is from 0 to', num_range
    print 'Number of remaining guesses is', num_guesses

def input_guess(guess):
    global num_guesses
    guess = int(guess)
    num_guesses -= 1
    print
    print 'Guess was', guess
    print 'Number of remaining guesses is', num_guesses

    if secret_number > guess:
        print 'Higher!'
    elif secret_number < guess:
        print 'Lower!'
    else:
        print 'Correct!'
        new_game()

    if num_guesses == 0:
        print 'You lose! The secret number was', secret_number, '. Try again.'
        new_game()

    
# create frame
f = simplegui.create_frame('Guess the number!', 200, 200)

# register event handlers for control elements and start frame
f.add_button('Range: 0-100', range100, 100)
f.add_button('Range: 0-1000', range1000, 100)
f.add_input('Enter guess:', input_guess, 100)

# call new_game 
range100()


# always remember to check your completed program against the grading rubric
