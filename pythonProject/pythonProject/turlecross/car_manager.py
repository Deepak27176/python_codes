from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def creat_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.goto(x=300, y=rand_y)
            self.all_car.append(new_car)


    def move_forward(self):
        for car in self.all_car:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



