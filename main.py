from turtle import Screen
from food import Food
from scoreboard import Score
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
score = Score()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 15:
        score.add_score()
        food.relocate()
        snake.extend()
    if snake.head.ycor() > 280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280:
        game_is_on = False
        score.game_is_over()
    for segment in snake.segments:
        if snake.head.distance(segment) < 10 and segment != snake.head:
            game_is_on = False
            score.game_is_over()

screen.exitonclick()
