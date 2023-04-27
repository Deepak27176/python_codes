from turtle import Turtle,Screen
import heroes
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
list1=["green yellow","dark red","purple","deep pink","gold"]


for i in range(3, 11):
    j=i
    k=360/i
    colour=random.choice(list1)
    timmy.color(colour)
    if i==3:
        timmy.forward(100)
        timmy.right(120)
        timmy.forward(100)
        timmy.right(120)
        timmy.forward(100)
        timmy.right(120)
    else:
        while j>0:
            timmy.forward(100)
            timmy.right(k)
            j=j-1



my_screen = Screen()
my_screen.exitonclick()
