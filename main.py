from turtle import Screen
from player import Player
from car import Car
from keep_score import KeepScore
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()
car = Car()
keep_score = KeepScore()

screen.listen()
screen.onkey(turtle_player.go_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    # Detect collision with car
    for index in car.car_list:
        if index.distance(turtle_player) < 20:
            game_on = False
            keep_score.game_over()

    # Detect successful crossing
    if turtle_player.player_finish():
        turtle_player.go_to_the_start()
        car.speed_level()
        keep_score.score_update()


screen.exitonclick()
