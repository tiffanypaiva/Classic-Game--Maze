from turtle import *
from random import random
from UtilitiesUsedForGames import line

def draw():
    "Draw a Maze."
    color('red')
    width(5)

    for X_Axis in range(-200, 200, 40):
        for Y_Axis in range(-200, 200, 40):
            if random() > 0.5:
                line(X_Axis, Y_Axis, X_Axis + 40, Y_Axis + 40)
            else:
                line(X_Axis, Y_Axis + 40, X_Axis + 40, Y_Axis)

    update()

def tap(X_Axis, Y_Axis):

    if abs(X_Axis) > 198 or abs(Y_Axis) > 198:
        up()
    else:
        down()

    width(2)
    color('blue')
    goto(X_Axis, Y_Axis)
    dot(4)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
