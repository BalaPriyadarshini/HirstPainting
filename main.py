import turtle as turtle_module
import random
from turtle import Screen

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
color_list = [(249, 248, 247), (235, 242, 240), (230, 235, 241), (2, 9, 30), (244, 238, 243), (122, 95, 42), (72, 32, 22), (237, 211, 72), (220, 81, 60), (225, 118, 101), (92, 1, 21), (178, 140, 170), (150, 92, 115), (34, 90, 27), (9, 153, 72), (204, 64, 92), (167, 129, 78), (2, 64, 146), (3, 78, 29), (6, 219, 217), (220, 179, 218), (79, 135, 179), (123, 154, 178), (80, 112, 139), (116, 188, 168), (7, 218, 224), (119, 14, 34), (242, 204, 8), (133, 224, 211), (230, 174, 165)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()