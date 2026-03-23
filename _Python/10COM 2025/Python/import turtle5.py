import turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)

turtles = []

def create_turtle():
    t = turtle.Turtle()
    t.speed(2)
    t.penup()
    t.goto(random.randint(-250, 250), random.randint(-250, 250))
    t.color(random.choice(["red", "blue", "green", "purple", "orange", "black"]))
    t.pendown()
    turtles.append(t)

for _ in range(5):
    create_turtle()

def move_turtles():
    for t in turtles:
        t.forward(random.randint(10, 30))
        t.setheading(random.randint(0, 360)) 
    
    screen.ontimer(move_turtles, 300)

