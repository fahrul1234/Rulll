import turtle
pen = turtle.Turtle()
turtle.speed('normal')
pen.pensize (4)

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

turtle.bgcolor('black')
pen.color('red','red')
pen.penup()

pen.goto(-550, -50)
pen.pendown()

def love():
    pen.left(136)
    pen.forward(100)
    curve()
    pen.left(120)
    curve()
    pen.forward(100)

pen.forward(200)

#huruf I
pen.left(90)
pen.fd(150)
pen.right(90)
pen.fd(50)
pen.right(90)
pen.fd(150)
pen.left(90)
pen.fd(150)

#love
love()

#huruf u
pen.left(144)
pen.fd(150)
for i in range (2):
    pen.fd(50)
    pen.left(90)
    pen.fd(150)
    pen.right(90)
    pen.fd(50)
    pen.right(90)
    pen.fd(150)
    pen.left(90)


pen.fd(200)

#titik i
pen.penup()
pen.goto(-325, 180)
pen.pendown()
pen.dot(50, 'red')
pen.penup()
pen.goto(-550, -70)
pen.pendown()
pen.ht()


turtle.done()