from turtle import Turtle
import random


COLORS = ["red", "blue", "yellow", "brown", "pink", "green", "black"]
START_SPEED = 5
SPEED = 15


class Car:

    def __init__(self):
        self.car_list = []
        self.move_speed = START_SPEED

    def create_car(self):
        random_select = random.randint(1, 7)
        if random_select == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_position_y = random.randint(-250, 250)
            car.goto(300, random_position_y)
            self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.backward(START_SPEED)

    def speed_level(self):
        self.move_speed += SPEED
