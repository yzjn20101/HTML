import turtle
import random
t = turtle.Turtle()
t.speed(3)
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
angles = [0, 90, 180, 270]
for _ in range(50):
    t.pencolor(random.choice(colors))
    t.forward(20)
    t.setheading(random.choice(angles))
turtle.done()
