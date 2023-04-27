from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 260)
        self.write(f"level:{self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"level:{self.level}", align="center", font=FONT)

    def game_up(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

