import turtle

turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(400,600)

star=turtle.Turtle()

length=100
angle=144

for i in range(5):
    star.forward(length)
    star.right(angle)
turtle.done()