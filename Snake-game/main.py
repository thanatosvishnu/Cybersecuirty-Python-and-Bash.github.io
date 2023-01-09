import time
from turtle import Screen
from snake import Snake
from food import Food
from Score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-game")
screen.tracer(0)

snakes = Snake()
New_food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()

    if snakes.head.distance(New_food) < 15:
        New_food.refresh()
        snakes.extend_segment()
        score.score += 1
        score.scores()
    if snakes.head.xcor() > 280 or snakes.head.xcor() < -280 or snakes.head.ycor() > 280 or snakes.head.ycor() < -280:
        score.reset()
        snakes.reset()

    for segment in snakes.segments[1:len(snakes.segments)]:
        if snakes.head.distance(segment) < 10:
            score.reset()
            snakes.reset()

screen.exitonclick()
