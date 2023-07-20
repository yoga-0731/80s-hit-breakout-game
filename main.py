from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

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
tiles = []
steps = 4
for step in range(steps):
    color = random.choice(COLORS)
    for i in range(10):
        tiles.append(Paddle((HORIZONTAL_LEFT + i * 40, VERTICAL_TOP), color, 2, 2))
    for i in range(9):
        tiles.append(Paddle((HORIZONTAL_RIGHT - i * 40, VERTICAL_TOP), color, 2, 2))
    VERTICAL_TOP -= 40


tile_objs = {}
for tile in tiles:
    tile_objs[tile.pos()] = tile

score = Scoreboard()

print(tile_objs)

screen.listen()
screen.onkey(paddle.right, 'Right')
screen.onkey(paddle.left, 'Left')

ball = Ball()

game_over = False
while not game_over:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    # Detect collision of the ball with the top wall and bounce the ball
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with right and left wall and bounce the ball
    if ball.xcor() > 360 or ball.xcor() < -380:
        ball.bounce_x()

    # Bounce and increase ball speed if the ball hits the paddle
    if ball.distance(paddle) < 40 and ball.ycor() < -250:
        ball.bounce_y()
        ball.increase_speed()

    # Delete the tile if the ball hits the tile and bounce the ball
    if ball.ycor() < 100:
        print(ball.pos())
    if ball.pos() in tile_objs:
        paddle.destroy_tile(tile_objs[(ball.xcor(), ball.ycor())])
        ball.bounce_y()
        score.increase_score()

    # Game over if paddle misses the ball
    if ball.distance(paddle) > 50 and ball.ycor() < -280:
        game_over = True

screen.exitonclick()

