from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.speed("fastest")
        self.goto(x=0, y=275)
        self.current_score = 0
        self.hideturtle()
        self.color("white")
        self.show_score()

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


