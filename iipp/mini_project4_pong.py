# Implementation of classic arcade game Pong

# Controls
# --------
# Player 1: W, S
# Player 2: up, down

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 15
PAD_WIDTH = 10
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_vel = [0, 0]
pad_vel = 3

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
# the ball's angle and velocity are variable within the given range
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120, 240) / 60.0
    ball_vel[1] = -random.randrange(60, 180) / 60.0

    if direction == LEFT:
        ball_vel[0] *= -1

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    score1 = score2 = 0
    paddle1_pos = paddle2_pos = HEIGHT / 2
    paddle1_vel = paddle2_vel = 0
    spawn_ball(random.choice([LEFT, RIGHT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # collide and reflect ball off top and bottom wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] *= -1
    elif ball_pos[1] > HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] *= -1
    
    # if ball hits either gutter, respawn ball moving in opposite direction
        # if paddle and ball collide, reflect, increase velocity by 10%, and update scores
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] > paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] > WIDTH - PAD_WIDTH - 1 - BALL_RADIUS:
        if ball_pos[1] > paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
        else:
            score1 += 1
            spawn_ball(LEFT)

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel > HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel > HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_line((HALF_PAD_WIDTH-2, paddle1_pos + HALF_PAD_HEIGHT), (HALF_PAD_WIDTH-2, paddle1_pos - HALF_PAD_HEIGHT), PAD_WIDTH, 'White')
    canvas.draw_line((WIDTH+2 - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), (WIDTH+2 - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), PAD_WIDTH, 'White')

    # draw scores
    canvas.draw_text(str(score1), (.4*WIDTH, .15*HEIGHT), 34, 'white')
    canvas.draw_text(str(score2), (.57*WIDTH, .15*HEIGHT), 34, 'white')

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['w']:
        paddle1_vel -= pad_vel
    elif key==simplegui.KEY_MAP['s']:
        paddle1_vel += pad_vel

    if key==simplegui.KEY_MAP['up']:
        paddle2_vel -= pad_vel
    elif key==simplegui.KEY_MAP['down']:
        paddle2_vel += pad_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['w'] or key==simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key==simplegui.KEY_MAP['up'] or key==simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button('Restart', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()