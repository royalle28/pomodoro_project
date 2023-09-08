from turtle import Turtle

FONT = ("Courier", 30, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.ht()
        self.current_score()
        self.high_score = 0

    def current_score(self):
        self.goto(0, 250)
        self.clear()
        self.write(arg=f"SCORE: {self.score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.current_score()

    def game_is_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.high_score = self.score
        self.score = 0