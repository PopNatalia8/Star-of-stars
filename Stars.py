import turtle

star = turtle.Turtle()
turtle.Screen().bgcolor("#994444")

star.penup()
star.goto((-200, 100))
star.pendown()
star.speed(20)
star.pensize(2)


def function(x, size):
    if size <= 10:
        return
    else:
        x.begin_fill()
        for i in range(5):
            star.forward(size)
            function(x, size/3)
            star.left(216)
        x.end_fill()


function(star, 360)

turtle.done()
