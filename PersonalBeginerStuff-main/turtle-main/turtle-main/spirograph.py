import turtle
import random
pen1 = turtle.Turtle()
pen1.speed(5)
display = turtle.Screen()
turtle.colormode(255)
turtle.bgcolor("black")
def color_choose():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def draw_circle():
    pen1.color(color_choose())
    pen1.circle(100)
    pen1.penup()
    pen1.right(10)
    pen1.pendown()
while True:
    draw_circle()
display.exitonclick()