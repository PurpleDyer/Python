import turtle

turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(100)
squary.pencolor("red")

for i in range(400):
    squary.forward(i)
    squary.left(91)
    squary.right(40)