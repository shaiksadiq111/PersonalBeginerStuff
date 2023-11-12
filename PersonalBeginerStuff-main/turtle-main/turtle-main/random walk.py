import turtle as t
import random

def color_maker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

pen1 = t.Turtle()
pen1.width(5)
display = t.Screen()
display.colormode(255)
t.bgcolor("black")
movements = [0, 1, 2, 3]
pen1.speed(2.5)
while True:
    color = color_maker()
    pen1.color(color)
    a = random.choice(movements)
    if a == 0:
        pen1.forward(50)
    elif a == 1:
        pen1.backward(50)
    elif a == 2:
        pen1.right(90)
        pen1.forward(50)
    elif a== 3:
        pen1.left(90)
        pen1.forward(50)
display.exitonclick()
