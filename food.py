from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.setx(random.randint(-280, 280))
        self.sety(random.randint(-280, 280))
