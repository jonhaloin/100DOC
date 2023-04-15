from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Jon's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for input key to move th snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


running = True
while running:

    # Updates the screen and moves the snake
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        scoreboard.refresh()
        snake.extend()

    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290):
        running = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            running = False

scoreboard.game_over()


screen.exitonclick()
