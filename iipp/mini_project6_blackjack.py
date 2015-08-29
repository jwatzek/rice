# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize globals
in_play = False
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = [str(card) for card in self.cards]
        return 'Hand contains: ' + ' '.join(s)

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # compute the value of the hand
        # aces = True, if the hand has at least one ace, then add 10 to hand value if it doesn't bust
        val = 0
        ace = False

        for card in self.cards:
            val += VALUES[card.rank]
            if card.rank == 'A':    ace = True
        if ace and val + 10 <= 21:  val += 10

        return val

    def draw(self, canvas, pos):
        for i, card in enumerate(self.cards):
            card.draw(canvas, (pos[0] + (CARD_SIZE[0] + 25) * i, pos[1]))

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        s = [str(card) for card in self.cards]
        return 'Deck contains: ' + ' '.join(s)


#define event handlers for buttons
def deal():
    global player, dealer, deck, in_play, outcome, score

    # if dealing while round is in play, player loses.
    if in_play:
        outcome = 'You gave up! Hit or stand?'
        score -= 1
    else:
        in_play = True
        outcome = 'Hit or stand?'

    # create and shuffle deck
    deck = Deck()
    deck.shuffle()

    # reset player and dealer hands
    # deal two cards each
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

def hit():
    global in_play, outcome, score

    # if the hand is in play, hit the player
    if in_play and player.get_value() <= 21:
        player.add_card(deck.deal_card())

    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = 'You busted! New deal?'
        in_play = False
        score -= 1
       
def stand():
    global in_play, outcome, score

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())

        if dealer.get_value() > 21:
            outcome = 'Dealer busted! New deal?'
            score += 1
        else:
            if player.get_value() <= dealer.get_value():
                outcome = 'Dealer wins! New deal?'
                score -= 1
            else:
                outcome = 'You win! New deal?'
                score += 1

    in_play = False


# draw handler    
def draw(canvas):
    canvas.draw_text('Blackjack', (60, 80), 38, 'Black')
    canvas.draw_text('Score: ' + str(score), (400, 80), 24, 'Black')
    canvas.draw_text('Dealer', (60, 140), 28, 'Black')
    canvas.draw_text('Player', (60, 320), 28, 'Black')
    dealer.draw(canvas, (60, 160))
    player.draw(canvas, (60, 340))
    canvas.draw_text(outcome, (150, 520), 28, 'Black')

    # if round is still in play, hide dealer's hole card
    # reveal when round is over
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [60 + CARD_CENTER[0], 160 + CARD_CENTER[1]], CARD_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()