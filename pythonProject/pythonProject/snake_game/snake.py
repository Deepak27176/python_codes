from turtle import Screen, Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for position in START_POSITIONS:
            self.add_position(position)


    def add_position(self, position):

        block = Turtle("circle")
        block.color("white")
        block.penup()
        block.goto(position)
        self.segments.append(block)

    def extend(self):
        self.add_position(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):  # this loop is to make all turtles to
            # follow the first turtle and Nth turtle will take (N-1)th turtle place
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]

