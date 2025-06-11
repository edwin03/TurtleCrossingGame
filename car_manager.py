import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.seth(180)
            new_car.goto(self.random_location())
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def random_location(self):
        return (300, random.randint(-250, 250))

    def move(self):
        for c in self.all_cars:
            c.forward(STARTING_MOVE_DISTANCE)

    def inc_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE *= MOVE_INCREMENT
        print(f"Move speed: {STARTING_MOVE_DISTANCE}")
