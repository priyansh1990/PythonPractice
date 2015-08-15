__author__ = 'Pri'

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# define draw handler
def draw(canvas):
    canvas.draw_circle([90, 200], 20, 10, "White")
    canvas.draw_circle([210, 200], 20, 10, "White")
    canvas.draw_line((50, 180), (250, 180), 40, "Red")
    canvas.draw_line((55, 170), (90, 120), 5, "Red")
    canvas.draw_line((90, 120), (130, 120), 5, "Red")
    canvas.draw_line((180, 108), (180, 160), 140, "Red")
    canvas.draw_line((200, 0), (0, 300), 10, "Green")

# create frame
frame = simplegui.create_frame("Text drawing", 200, 300)

# register draw handler
frame.set_draw_handler(draw)



# start frame
frame.start()