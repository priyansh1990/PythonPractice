__author__ = 'Pri'

import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("yellow")

    for i in range(1,5,1):
            brad.forward(100)
            brad.right(90)

    window.exitonclick()

draw_square()

def draw_circle():

    window = turtle.Screen()
    window.bgcolor("red")

    angie=turtle.Turtle()
    angie.circle(50)
    angie.color("yellow")
    angie.pencolor("pink")
    window.exitonclick()


draw_circle()


def draw_triangle():

    window = turtle.Screen()
    window.bgcolor("red")

    triangle=turtle.Turtle()

    window.exitonclick()


draw_triangle()