from turtle import Turtle
SEGMENT_SIZE = 20
STARTING_POSITION = (0, 0)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.length = 3
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for i in range(self.length):
            self.add_segment()
            # Moves each segment to the appropriate starting position
            self.segments[i].goto(-SEGMENT_SIZE * (i + STARTING_POSITION[0]), STARTING_POSITION[1])

    def add_segment(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape('square')
        new_segment.color('white')
        self.segments.append(new_segment)
        self.length = len(self.segments)

    def extend(self):
        self.add_segment()
        self.segments[self.length - 1].goto(self.segments[-2].position())

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
