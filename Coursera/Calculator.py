__author__ = 'Pri'

# calculator with all buttons


import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# intialize globals
store = 0
operand = 0


# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""


def swap():
    global store, operand
    store, operand = operand, store
    output()


def add():
    """ add operand to store"""
    global store
    store += operand
    output()


def sub():
    """ subtract operand from store"""
    global store
    store -= operand
    output()


def multi():
    """ multiply store by operand"""
    global store
    store *= operand
    output()


def div():
    """ divide store by operand"""
    global store
    store /= operand
    output()


def enter(inp):
    """
global put in fron to srpeci

    :param inp:
    """
    global operand
    operand = float(inp)
    output()

# create frame
f = simplegui.create_frame("Calculator", 300, 300)

# register event handlers
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Multi", multi, 100)
f.add_button("Div", div, 100)
f.add_input("Enter Operand", enter, 100)


# get frame rolling
f.start()