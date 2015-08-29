# Stopwatch: The Game
import simplegui
import random

# define global variables
time = 0
num_stop = 0
num_hit = 0

# define helper function
def format(time):
    """Converts the time from tenths of seconds to A:BC.D format."""
    A = time / 600
    time %= 600
    B = time / 100
    C = time % 100 / 10
    D = time % 10

    return str(A) + ':' + str(B) + str(C) + '.' + str(D)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    """Starts the stopwatch."""
    timer.start()

def stop():
    """Stops the stopwatch."""
    global num_stop, num_hit
    if timer.is_running():
        num_stop += 1
        if time % 10 == 0:
            num_hit += 1
    timer.stop()

def reset():
    """Resets the stopwatch to zero."""
    global time, num_stop, num_hit
    num_stop = 0
    num_hit = 0
    time = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    """Increment global time in tenths of seconds. Maximum time is 9:59:9."""
    global time
    if time < 5999:  time += 1
    else:            timer.stop()

# define draw handler
def draw(canvas):
    """Write formatted time in canvas."""
    canvas.draw_text(format(time), [40, 115], 48, 'Red')
    canvas.draw_text(str(num_hit) + '/' + str(num_stop), [140, 40], 32, 'Green')
    
# create frame
f = simplegui.create_frame('Stopwatch: The Game', 200, 200)
f.set_draw_handler(draw)

# create timer with 0.1 second interval
timer = simplegui.create_timer(100, tick)

# register event handlers
f.add_button('Start', start, 100)
f.add_button('Stop', stop, 100)
f.add_button('Reset', reset, 100)


# start frame
f.start()