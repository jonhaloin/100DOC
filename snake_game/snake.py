from turtle import Turtle
SEGMENT_SIZE = 20
STARTING_POSITION = (0,0)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.length = 3
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for i in range(self.length):
            self.segments.append(Turtle())
            self.segments[i].penup()
            self.segments[i].shape('square')
            self.segments[i].color('white')
            self.segments[i].goto(-SEGMENT_SIZE * (i + STARTING_POSITION[0]), STARTING_POSITION[1])

    def move(self):
        for i in range(self.length - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.segments[0].forward(SEGMENT_SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)