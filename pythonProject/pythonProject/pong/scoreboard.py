from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.l_game = " left player won the game"
        self.r_game = " right player won the game"

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center",font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_scoreup(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_scoreup(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def l_gameover(self):
        self.goto(0, 0)
        self.write(self.l_game, align="center", font=("Courier", 20, "normal"))

    def r_gameover(self):
        self.goto(0, 0)
        self.write(self.r_game, align="center", font=("Courier", 20, "normal"))


