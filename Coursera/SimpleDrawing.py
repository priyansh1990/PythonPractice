__author__ = 'Pri'

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!",[100, 100], 24, "Red")
    canvas.draw_circle([100, 100], 1, 2, "White")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw handler
frame.set_draw_handler(draw)

# start frame
frame.start()