from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Arial", 36, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(60, 240)
        self.write(f"{self.score_right}", align=ALIGNMENT, font=FONT)
        self.goto(-60, 240)
        self.write(f"{self.score_left}", align=ALIGNMENT, font=FONT)

    def increase_right_score(self):
        self.score_right += 1
        self.update_scoreboard()

    def increase_left_score(self):
        self.score_left += 1
        self.update_scoreboard()