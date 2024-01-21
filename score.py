from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        with open("snakefile.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.sety(279)
        self.color("white")
        self.scoree = 0
        self.write(arg=f"SCORE: {self.scoree}   RECORD: {self.highscore}", align="center", font=("Arial", 15, "normal"))

    def score(self):
        self.scoree = self.scoree + 1
        self.clear()
        self.write(arg=f"SCORE: {self.scoree}   RECORD: {self.highscore}", align="center", font=("Arial", 15, "normal"))

    def over(self):
        if self.highscore < self.scoree:
            self.highscore = self.scoree
        with open("snakefile.txt", mode="w") as file:
            file.write(f"{self.highscore}")
        self.clear()
        self.scoree = 0
        self.write(arg=f"SCORE: {self.scoree}   RECORD: {self.highscore}", align="center", font=("Arial", 15, "normal"))

