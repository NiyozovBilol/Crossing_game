import turtle
from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        turtle.colormode(255)
        self.cars = []
        self.color_generator()
        self.move_distance = 5

    def create(self):
        bill = Turtle("square")
        bill.color(self.color_generator())
        bill.penup()
        bill.shapesize(stretch_wid=1, stretch_len=2)
        bill.goto(300, random.randint(-240, 240))
        bill.setheading(180)
        self.cars.append(bill)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def color_generator(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r,g,b)

    def update_speed(self):
        self.move_distance = 10