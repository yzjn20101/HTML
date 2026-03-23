import turtle
import random

t = turtle.Turtle()
t.speed(3)  

angles = [0, 90, 180, 270]

for _ in range(50):  
    t.forward(20) 
    t.setheading(random.choice(angles)) 
turtle.done()
