from turtle import Turtle
MOVE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1/2, stretch_len=5)
        self.penup()
        self.goto(position)

    def right(self):
        xcor = self.xcor() + MOVE
        self.goto(xcor, self.ycor())

    def left(self):
        xcor = self.xcor() - MOVE
        self.goto(xcor, self.ycor())
