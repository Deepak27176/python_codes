import turtle
from turtle import Turtle, Screen
import random
racers = ["sai", "sat", "krish", "brahm", "damu", "naidu"]
color = ["red", "green", "purple", "violet", "yellow", "blue"]
race=[]
y_pos = [0,20,40,60, 80, 100]
is_race_on = False

my_screen = Screen()
my_screen.setup(width=500, height=400)



for i in range(0, 6):
    racers[i] = Turtle(shape="turtle")
    racers[i].penup()
    racers[i].color(color[i])
    racers[i].goto(x=-230, y=y_pos[i])
    race.append(racers[i])
user_bet = my_screen.textinput(title="make bet", prompt="whose gonna win the race")
if user_bet:
    is_race_on = True
while is_race_on:
    i=0
    for guys in race:


        if guys.xcor() > 230:
            is_race_on=False
            winner = guys.pencolor()

            if winner == user_bet:
                print(f"you won the bet {winner} turtle won the race")
            else:
                print(f"you lost the bet {winner} turtle won the race")
        movement = random.randint(0, 10)
        guys.forward(movement)
my_screen.exitonclick()
