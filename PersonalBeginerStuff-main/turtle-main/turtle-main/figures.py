import turtle as t
import random
def color_maker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
pen1 = t.Turtle()
pen1.speed(1)
pen1.pensize(8)
display = t.Screen()
display.colormode(255)
t.bgcolor("black")
def set_position():
    pen1.penup()
    pen1.forward(90)
    pen1.right(90)
    pen1.forward(300)
    pen1.right(90)
    pen1.pendown()
def do():
    for i in range(3,9):
        angle = 360/ i
        for _ in range(i):
            color = color_maker()
            pen1.color(color)
            pen1.forward(200)
            pen1.right(angle)
set_position()
do()
display.exitonclick()
