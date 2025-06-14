from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)
    
    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def start(self):
        self.goto(STARTING_POSITION)
