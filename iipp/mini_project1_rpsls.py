# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    if name == 'rock':
        num = 0
    elif name == 'Spock':
        num = 1
    elif name == 'paper':
        num = 2
    elif name == 'lizard':
        num = 3
    elif name == 'scissors':
        num = 4
    else:
        print 'Invalid choice.'
    return num


def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print 'Number is out of range.'
    return name
    

def rpsls(player_choice): 
    print
    
    # player choice
    print 'Player chooses', player_choice
    player_number = name_to_number(player_choice)
    
    # computer choice
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print 'Computer chooses', comp_choice
    
    # compute difference
    diff = (comp_number - player_number) % 5
    
    # determine winner, print winner message
    if diff == 0:
        print 'Player and computer tie!'
    elif diff > 2:
        print 'Player wins!'
    else:
        print 'Computer wins!'
    return

    
# testing the code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



