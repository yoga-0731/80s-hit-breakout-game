from turtle import Turtle

FONT = ('Arial', 14, 'normal')
POSITION = (0, 280)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(POSITION)
        self.print_score()

    def increase_score(self):
        self.clear()
        self.goto(POSITION)
        self.score += 1
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", align='center', font=FONT)
