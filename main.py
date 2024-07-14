import turtle as t
import random

color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181), (148, 116, 120), (204, 183, 186), (180, 195, 200), (53, 69, 59), (122, 129, 135)]

kratos = t.Turtle()

t.colormode(255)


kratos.shapesize(1)
kratos.speed(9)


def positioning(x, y):
    kratos.penup()
    kratos.hideturtle()
    kratos.setposition(x, y)
    kratos.pendown()


def paint():
    for _ in range(9):
        kratos.color(random.choice(color_list))
        kratos.dot(20)
        kratos.penup()
        kratos.forward(50)
        kratos.dot(20)


yaxis = -250

for ppp in range(10):
    positioning(-260, yaxis)
    paint()
    yaxis += 50


















screen = t.Screen()
screen.exitonclick()