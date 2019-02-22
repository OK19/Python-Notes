import turtle
bob = turtle.Turtle()

def square(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

square(bob, 100000, .1)
turtle.mainloop()
