# Example Mini-Project:
# THE MYSTICAL OCTOSPHERE! by Andrea Crain

# This game is based on a common toy. It is a 
# round black ball with a clear plastic window. 
# The ball is filled with murky blue liquid
# and you use it as a fortune teller. You ask 
# a yes-or-no question and shake the ball. There 
# is a white many-sided die inside with answers, 
# and when you stop shaking, one of the sides
# floats up and is readable against the window.

import random

# helper function

def number_to_fortune(number):
    if number == 0:
        fortune = 'Yes, for sure!'
    elif number == 1:
        fortune = 'Probably yes.'
    elif number == 2:
        fortune = 'Seems like yes...'
    elif number == 3:
        fortune = 'Definitely not!'
    elif number == 4:
        fortune = 'Probably not.'
    elif number == 5:
        fortune = 'I really doubt it...'
    elif number == 6:
        fortune = 'Not sure, check back later!'
    elif number == 7:
        fortune = "I really can't tell"
    else:
        fortune = 'Invalid input.'
    return fortune

    
def mystical_octosphere(question):
    print 'Your question was...', question
    print 'You shake the mystical octosphere.'    

    answer_number = random.randrange(8)
    answer_fortune = number_to_fortune(answer_number)
    print 'The cloudy liquid swirls, and a reply comes into view...'
    print 'The mystical octosphere says...', answer_fortune
    print

    return   
    
# These lines runs your main function!
# You can change the questions if you wish.
# Only yes-or-no style questions will make sense.
mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")


