from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))



