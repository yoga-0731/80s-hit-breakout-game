from turtle import Turtle
MOVE = 20


class Paddle(Turtle):

    def __init__(self, position, color='white', width=1/2, length=5):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.pencolor('white')
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.penup()
        self.goto(position)

    def right(self):
        xcor = self.xcor() + MOVE
        self.goto(xcor, self.ycor())

    def left(self):
        xcor = self.xcor() - MOVE
        self.goto(xcor, self.ycor())

    def destroy_tile(self, tile):
        tile.hideturtle()
