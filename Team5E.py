import turtle
#---~
t = turtle.Turtle()

t.left(90)

t.forward(50)
for i in range(180):
    t.right(1)
    t.forward(1)
t.forward(50)

t.right(90)
t.forward(60)
t.left(90)

t.forward(50)
for i in range(180):
    t.right(1)
    t.forward(1)
t.forward(50)

t.right(90)
t.forward(50)

while True:
    turtle.penup()
