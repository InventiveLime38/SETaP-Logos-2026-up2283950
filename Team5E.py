import turtle
#---~

#setperameters
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("StudentSplit Logo Lem")
screen.setup(width=330, height=330)
len = 60
step = len//20
turnr = 90
t.color("navyblue")
t.width(5)
#---~

#drawoutercircle
t.fillcolor("#FF8C00")
t.begin_fill()
t.penup()
t.goto(0, -140)
t.pendown()
t.circle(140)
t.end_fill()
#---~

#prepareforlogo
t.penup()
t.goto(-len//2, len//2)
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
#---~

#createlogo
t.left(turnr)
for i in range(turnr * 3):
    t.right(1)
    t.forward(1.1)
t.right(turnr)
t.forward(len)
t.right(turnr)
t.forward(step)
t.backward(step)
t.right(turnr)
t.forward(len)
for i in range(turnr * 3):
    t.right(1)
    t.forward(1.1)
t.right(turnr)
t.forward(len)
t.right(turnr)
t.forward(step)
t.backward(step)
t.right(turnr)
t.forward(len)
#---~

#disappear
t.end_fill()
t.hideturtle()
turtle.done()
#---~