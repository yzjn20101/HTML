import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()
t.speed(2)

border_x = screen.window_width() // 2 - 10
border_y = screen.window_height() // 2 - 10

def move():
    t.forward(20)
    x, y = t.pos()

    if abs(x) > border_x or abs(y) > border_y:
        t.right(180)

    screen.ontimer(move, 200)

move()
screen.mainloop()
