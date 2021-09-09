import turtle

i = 0
while (i <= 5):
    turtle.penup()
    turtle.goto(0, i * 100)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(i * 100, 0)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(500)
    turtle.right(90)
    i += 1

turtle.exitonclick()
