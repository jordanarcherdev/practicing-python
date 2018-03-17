import turtle

def drawASquare(whichTurtle):
    color = ('Pink')
    for loopCounter in range(4):
        whichTurtle.forward(150)
        whichTurtle.right(90)

window = turtle.Screen()
timmy = turtle.Turtle()
timmy.speed(0)
timmy.color("red")

for loopCounter in range(72):
    drawASquare(timmy)
    timmy.left(5)

window.exitonclick()
