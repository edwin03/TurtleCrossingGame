import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.

player1 = Player()
screen.onkeypress(player1.up, "Up")

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    # Detect when the turtle player collides with a car and stop the game if this happens.
    for c in cars.all_cars:
        if c.distance(player1) < 20:
            print("Game Over")
            game_is_on = False
    #         #scoreboard = Scoreboard()
    #         #scoreboard.game_over()
    # current_position = player1.position()
    # if current_position[1] >= 280:
    #     player1.start()
    #     cars.clear()
    #     screen.clear()

    # Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.
