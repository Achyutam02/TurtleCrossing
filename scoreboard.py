from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("black")
        self.update()


    def update(self):
        self.goto(-240, 270)
        self.write(f"Level : {self.score}", font=("Courier", 15, "normal"))
        self.goto(100, 270)
        self.write(f"High Score = {self.high_score}", font=("Courier", 15, "normal"))

    def update_screen(self):
        self.score += 1
        self.clear()
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER ")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.clear()
        self.update()





