import turtle
import random

t = turtle.Turtle()
t.speed(3)

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

angles = [0, 90, 180, 270]

distances = [10, 20, 30, 40, 50]

for _ in range(50):  
    t.pencolor(random.choice(colors))
    t.forward(random.choice(distances))
    t.setheading(random.choice(angles))
turtle.done()
