# import colorgram
# rgb_color = []
# colors = colorgram.extract('colordot.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)

#print(rgb_color)
import turtle
from turtle import Turtle,Screen
import random
tim = Turtle()
turtle.colormode(255)
color = [(239, 242, 247), (197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180), (131, 34, 23), (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80), (165, 147, 157), (21, 92, 68), (28, 59, 75), (225, 177, 167), (59, 44, 46), (133, 29, 33), (180, 202, 179), (26, 84, 89), (88, 147, 129), (13, 70, 58), (42, 65, 89), (180, 99, 102), (216, 181, 186), (182, 191, 204)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range(0,10):
    for j in range(0,10):
        tim.dot(20, random.choice(color))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
my_screen = Screen()
my_screen.exitonclick()





