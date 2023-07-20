from turtle import Screen
from paddle import Paddle
import random

COLORS = ['green', 'navy', 'maroon', 'violet', 'gray']
HORIZONTAL_LEFT = -360
HORIZONTAL_RIGHT = 360
VERTICAL_TOP = 240

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)

paddle = Paddle((0, -250))
steps = 4
for step in range(steps):
    color = random.choice(COLORS)
    for i in range(10):
        Paddle((HORIZONTAL_LEFT + i * 40, VERTICAL_TOP), color, 2, 2)
    for i in range(9):
        Paddle((HORIZONTAL_RIGHT - i * 40, VERTICAL_TOP), color, 2, 2)
    VERTICAL_TOP -= 40


screen.listen()
screen.onkey(paddle.right, 'Right')
screen.onkey(paddle.left, 'Left')

game_over = False
while not game_over:
    screen.update()


screen.exitonclick()
