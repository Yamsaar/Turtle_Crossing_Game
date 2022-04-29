from turtle import Turtle

FONT = ("Courier", 24, "normal")


class KeepScore(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level} ", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
