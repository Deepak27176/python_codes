from turtle import Turtle ,Screen
tim = Turtle()

def mov_for():
    tim.forward(15)
def mov_back():
    tim.backward(15)
def turn_left():
    #new_head=tim.heading()*10
    #tim.setheading(new_head)
    tim.right(10)
def turn_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


my_screen = Screen()
my_screen.listen()
my_screen.onkey(key="w", fun=mov_for)
my_screen.onkey(key="s", fun=mov_back)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=clear)
my_screen.exitonclick()
