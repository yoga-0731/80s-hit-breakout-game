from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, -250)
        self.xmove = 5
        self.ymove = 5
        self.ball_speed = 0.05

    def move(self):
        self.goto(self.xcor()+self.xmove, self.ycor()+self.ymove)

    def bounce_x(self):
        self.xmove *= -1
        self.ball_speed *= 0.9

    def bounce_y(self):
        self.ymove *= -1
        self.ball_speed *= 0.9

    def increase_speed(self):
        self.speed()

