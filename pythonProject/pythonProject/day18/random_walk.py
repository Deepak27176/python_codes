import turtle
from turtle import Turtle,Screen
import random
list2 = [0,90,180, 270,360]
j = random.choice(list2)
tom = Turtle()
k = 500
tom.width(6)
turtle.colormode(255)
tom.speed("fastest")
def colour_set():
    r=random.randint(0,255)
    y = random.randint(0, 255)
    b = random.randint(0, 255)
    set = (r, y, b)
    return set


while k>0:

    tom.color(colour_set())
    j = random.choice(list2)
    tom.forward(20)
    tom.setheading(j)
    k -= 1

my_screen = Screen()
my_screen.exitonclick()
while j<=360:
    tom.color(colour_set())
    tom.circle(100)
    tom.setheading(j+1)
    j += 1