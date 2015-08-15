__author__ = 'Pri'


# define global variables
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

interval = 100
count = 0
total_stops = 0
success_stops = 0
stop = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    milli_sec = t % 10
    sec = int(t // 10) % 10
    d = (t // 100)
    ten_sec = int(d) % 6
    aa = t // 600
    minutes = int(aa) % 600
    string = str(minutes) + ":" + str(ten_sec) + str(sec) + "." + str(milli_sec)
    return string


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global count, stop
    stop = False
    timer.start()


def stopButton():
    global total_stops, success_stops, stop
    if not stop:
        if count % 10 == 0 and count != 0:
            success_stops += 1
            total_stops += 1
        elif count != 0:
            total_stops += 1
    stop = True
    timer.stop()


def reset():
    global count, success_stops, total_stops, stop
    count = 0
    stop = True
    total_stops = 0
    success_stops = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1

# define draw handler
def draw(canvas):
    text = format(count)
    canvas.draw_text(text, (80, 125), 42, "white")
    canvas.draw_text(str(success_stops) + '/' + str(total_stops), (190, 30), 24, "pink")

# Create a frame
frame = simplegui.create_frame("Stopwatch game", 250, 250)
frame.set_canvas_background('green')

# Register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stopButton, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
reset()
