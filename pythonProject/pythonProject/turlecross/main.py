import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(player.move, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.creat_car()
    car_manager.move_forward()

    # Detect collision with car
    for car in car_manager.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_up()
    # Detect crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
