from turtle import Turtle


class Snake:

    def __init__(self):
        self.body = []
        self.createbody()

    def createbody(self):
        x = 0
        for i in range(0, 3):
            bodyy = Turtle(shape="square")
            bodyy.penup()
            bodyy.color("white")
            bodyy.setx(x)
            x = x - 20
            self.body.append(bodyy)

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].goto(x, y)
        self.body[0].forward(20)

    def growth(self):
        bodyy = Turtle(shape="square")
        bodyy.penup()
        bodyy.color("white")
        x = self.body[-1].xcor()
        y = self.body[-1].ycor()
        bodyy.setx(x)
        bodyy.sety(y)
        self.body.append(bodyy)

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def game(self):
        if self.body[0].xcor() > 280 or self.body[0].ycor() > 290 or self.body[0].xcor() < -280 or self.body[0].ycor() < -290:
            for i in self.body:
                i.goto(1000,1000)
            self.body.clear()
            self.createbody()

        for i in self.body[1:]:
            if self.body[0].distance(i) < 15:
                for i in self.body:
                    i.goto(1000, 1000)
                self.body.clear()
                self.createbody()


        return True
