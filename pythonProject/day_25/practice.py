import turtle
import random
col = ["red", "blue", "green", "yellow", "pink"]
tim = turtle.Turtle()
my_screen = turtle.Screen()
tim.shape("turtle")
k = 36
while k > 0:
    tim.color(random.choice(col))
    tim.circle(20)
    tim.forward(10)
    tim.right(10)
    k -= 1


my_screen.mainloop()
