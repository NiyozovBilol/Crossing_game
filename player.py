from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def reset_pos(self):
        self.goto(0, -280)
