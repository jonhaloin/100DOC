from turtle import Turtle
FONT = ('Arial', 30, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")

        self.refresh()

    def increase(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
