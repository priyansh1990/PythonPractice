__author__ = 'Pri'

import turtle


def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    windows = turtle.Screen()
    windows.bgcolor("red")

    # create square
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(500)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    #create a circle

    angie = turtle.Turtle()
    angie.speed(50)

    for i in range(0,36):
         angie.circle(100)
         angie.right(10)
    angie.color("blue")
    angie.shape("circle")
    angie.right(90)
    angie.forward(200)




    windows.exitonclick()


draw_art()
