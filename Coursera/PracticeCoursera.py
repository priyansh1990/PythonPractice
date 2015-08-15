# convert xx.yy to xx dollars and yy cents
def convert(val):
    dollars = int(val)
    cents = float(100 * (val - dollars))
    return str(dollars) + " dollars and " + str(cents) + " cents"


# Tests
# print convert(11.23)
# print convert(11.20)
# print convert(1.12)
# print convert(12.01)
# print convert(1.01)
# print convert(0.01)
# print convert(1.00)
# print convert(0)
# print convert(-1.40)
# print convert(12.55555)
#
# int("five")
# word ="1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1"
# print word.count("l")
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#
# def timer_handler():
# print("I")
#
# timer = simplegui.create_timer(1000, timer_handler)
# timer.start()

# int("5.4")


global state

result = 1
iteration = 0
max_iterations = 10

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n


def get_next(current):
    """???  Part of mystery computation."""
    return 0.5 * (current + n / current)


# timer callback

def update():
    """???  Part of mystery computation."""
    global iteration, result
    iteration += 1
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", result
    else:
        result = get_next(result)

# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(16)
timer.start()

import time
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

# from rockstar import RockStar
#
# python_code = "print('Hello world')"
# rock_it_bro = RockStar(days=400, file_name='helloWorld.py', code=python_code)
# rock_it_bro.make_me_a_rockstar()

