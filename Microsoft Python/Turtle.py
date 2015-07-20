__author__ = 'Pri'

import turtle

nbSides=12

for steps in range(nbSides):
    turtle.forward(100)
    turtle.right(360/nbSides)

    for moreSteps in range(nbSides):
        turtle.forward(50)
        turtle.right(360/nbSides)



# for name in range(4):
#     turtle.forward(10)
#     turtle.right(90)
#     for steps in range(4):
#         turtle.forward(50)
#         turtle.right(90)



turtle.getscreen()._root.mainloop()