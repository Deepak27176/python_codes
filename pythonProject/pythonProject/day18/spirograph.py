import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
tom = Turtle()
tom.speed("fastest")
def colour_set():
    r=random.randint(0,255)
    y = random.randint(0, 255)
    b = random.randint(0, 255)
    set = (r, y, b)
    return set
j=0
tom.circle(100)
tom.left(90)
tom.forward(50)
tom.right(90)
tom.circle(50)
tom.right(270)
while j<=360:
    tom.color(colour_set())
    tom.circle(50)
    tom.setheading(j+1)
    j += 1


My_screen=Screen()
My_screen.exitonclick()