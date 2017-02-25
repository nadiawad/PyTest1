import turtle


def draw_square():
    myTurtle = turtle.Turtle()
    myTurtle.shape("turtle")
    myTurtle.color("white")
    myTurtle.speed(1)
    myTurtle.fill(True)

    for i in range(0,4):
        myTurtle.forward(100)
        myTurtle.right(90)
    myTurtle.fill(False)


def draw_circle():
    mySecondTurtle = turtle.Turtle()
    mySecondTurtle.shape('arrow')
    mySecondTurtle.color('yellow')
    mySecondTurtle.circle(50)
    mySecondTurtle.speed(2)


def draw_triangle():
    myThirdTurtle = turtle.Turtle()
    myThirdTurtle.shape('circle')
    myThirdTurtle.forward(100)
    myThirdTurtle.color('red')
    for i in range(0,3):
        myThirdTurtle.forward(100)
        myThirdTurtle.right(120)
    myThirdTurtle.speed(2)


def draw_my_shape():
    myTurtle = turtle.Turtle()
    myTurtle.shape("turtle")
    myTurtle.forward(100)
    myTurtle.color("yellow")
    myTurtle.speed(0)
    loop_id=1
    while loop_id <= 360:
        for i in range(0,4):
            myTurtle.forward(100)
            myTurtle.right(90)
        myTurtle.right(1)
        loop_id+=1
        print loop_id
window = turtle.Screen()
window.bgcolor("black")

#draw_square()
#draw_circle()
#draw_triangle()
draw_my_shape()

window.exitonclick()