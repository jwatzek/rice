# implementation of card game - Memory
import simplegui
import random

# create deck of 2 pairs of 8 cards with numbers 0-7
deck = range(8)*2

# set x coordinates of cards
xpos = []
for i in range(16):
	xpos.append((i*50, (i+1)*50))

# initialize globals
def new_game():
	global state, turns, exposed, card1, card2
    random.shuffle(deck)
    state = turns = 0
    exposed = [False]*16
	card1 = card2 = None

# define event handlers
def mouseclick(pos):
    global state, turns, exposed, card1, card2

    for idx in range(16):
        if pos[0] >= xpos[idx][0] and pos[0] < xpos[idx][1]:
            card = idx
            
            # do nothing if exposed card is clicked
		    if exposed[card]:	return
            
            exposed[card] = True
            break

    # game state logic
    if state == 0:
        state = 1
        card1 = card
    elif state == 1:
        turns += 1
        state = 2
    	card2 = card
    else:
        state = 1

        if deck[card1] != deck[card2]:
            exposed[card1] = exposed[card2] = False
        card1 = card
                        
# cards are 50x100 pixels in size
def draw(canvas):
    for card in range(16):
    	if exposed[card]:
    		canvas.draw_text(str(deck[card]), (card*50+15, 60), 36, 'White')
    	else:
    		canvas.draw_polygon([(xpos[card][0], 0), (xpos[card][0], 100), (xpos[card][1], 100), (xpos[card][1], 0)], 2, 'Black', 'Green')

    label.set_text('Turns = ' + str(turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()