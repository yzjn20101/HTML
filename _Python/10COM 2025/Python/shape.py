import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)

t.penup()
t.goto(0, -100)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-30, 40)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(30, 40)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.color("black")

t.penup()
t.goto(-25, 50)
t.pendown()
t.begin_fill()
t.circle(4)
t.end_fill()

t.penup()
t.goto(35, 50)
t.pendown()
t.begin_fill()
t.circle(4)
t.end_fill()

t.penup()
t.goto(-40, 0)
t.pendown()
t.setheading(-60)
t.circle(40, 120)

t.hideturtle()
screen.mainloop()
