import turtle

ninja = turtle.Turtle()

ninja.speed(100)

a=['red','blue','green','black']
j=0

for i in range(500):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)


    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    ninja.right(10)

turtle.done()