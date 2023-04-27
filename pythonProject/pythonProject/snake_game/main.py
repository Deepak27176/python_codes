from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score_board import Scoreboard
my_screen = Screen()

my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
segments = []
my_screen.tracer(0)

snake = Snake()     # Turn turtle animation on/off and set delay
food = Food()
my_screen.listen()
scoreboard = Scoreboard()
my_screen.onkey(snake.Up, "Up")
my_screen.onkey(snake.Down, "Down")  # assigning arrow keys to control snake direction
my_screen.onkey(snake.Left, "Left")
my_screen.onkey(snake.Right, "Right")
is_game_on = True
while is_game_on:
    my_screen.update()  # Perform a TurtleScreen update edhi esthe screen update ayyi malli agipothadi
    time.sleep(0.2)       # screen update ni delay chesthadi so snake body slow ga move avthadi
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detection with collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

        # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()

my_screen.exitonclick()
