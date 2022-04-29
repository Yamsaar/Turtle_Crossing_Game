from turtle import Turtle

UP = 90
Move = 10
STARTING_POINT = (0, - 280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_the_start()
        self.setheading(UP)

    def go_up(self):
        self.forward(Move)

    def go_to_the_start(self):
        self.goto(STARTING_POINT)

    def player_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False
