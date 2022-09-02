from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []

for _ in range(3):
    x_position = [0, -20, -40]
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.pu()
    new_segment.goto(x=x_position[_], y=0)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(15)
    segments[0].left(30)

screen.exitonclick()
