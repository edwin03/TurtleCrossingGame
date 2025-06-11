import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.seth(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(self.random_location())
        self.color(random.choice(COLORS))

    def random_location(self):
        return (300, random.randint(-250, 250))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
    
    def inc_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE *= MOVE_INCREMENT
        print(f"Move speed: {STARTING_MOVE_DISTANCE}")
