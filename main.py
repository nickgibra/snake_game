import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoree = Score()

screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")


while snake.game():
    screen.update()
    time.sleep(0.1)
    snake.move()
    for i in range(0, len(snake.body)):
        if snake.body[0].distance(food) < 15:
            food.refresh()
            scoree.score()
            snake.growth()
        if snake.body[0].xcor() > 280 or snake.body[0].ycor() > 290 or snake.body[0].xcor() < -280 or snake.body[0].ycor() < -290:
            scoree.over()
        for i in snake.body[1:]:
            if snake.body[0].distance(i) < 15:
                scoree.over()



screen.exitonclick()
