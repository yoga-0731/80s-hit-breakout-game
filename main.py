from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)

paddle = Paddle((0, -250))

screen.listen()
screen.onkey(paddle.right, 'Right')
screen.onkey(paddle.left, 'Left')

game_over = False
while not game_over:
    screen.update()


screen.exitonclick()
