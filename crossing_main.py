from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("COME TO TOP, IF YOU CAN~~~")
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")

increment = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if increment % 5 == 0:
        car.create()
    car.move()
    increment += 1

    # Detecting if the turtle reaches the top
    if player.ycor() > 280:
        scoreboard.update_level()
        player.reset_pos()
        car.update_speed()

    # Detecting if turtle crashes with a car
    for item in car.cars:
        if player.distance(item) < 22:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
