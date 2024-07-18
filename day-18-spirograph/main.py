import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("black", "red")
tim.pensize(2)

def random_colour():
    turtle.colormode(255)
    R = random.randrange(0, 255)
    G = random.randrange(0, 255)
    B = random.randrange(0, 255)
    return R, G, B


#Random walk
def random_walk():
    angles = [0, 90, 180, 270]
    direction = random.choice(angles)
    tim.speed(0)
    tim.pencolor(random_colour())
    tim.setheading(direction)
    tim.forward(30)


#spirograph
def spirograph(angle):
    tim.setheading(angle)
    tim.speed(0)
    tim.pencolor(random_colour())
    tim.circle(100)


for angle in range(0, 361, 4):
    spirograph(angle)


screen = Screen()
screen.exitonclick()
