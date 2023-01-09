from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=-20, y=280)
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.scores()
        self.reset()

    def scores(self):
        self.clear()
        self.write(f"Score : {self.score}  High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.scores()