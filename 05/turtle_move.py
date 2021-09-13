import turtle

def move():
	turtle.forward(50)
	turtle.stamp()

def move_w():
	turtle.setheading(90)
	move()

def move_a():
	turtle.setheading(180)
	move()

def move_s():
	turtle.setheading(270)
	move()

def move_d():
	turtle.setheading(0)
	move()

def restart():
	turtle.reset()

turtle.shape('turtle')
turtle.onkey(move_w, 'w')
turtle.onkey(move_a, 'a')
turtle.onkey(move_s, 's')
turtle.onkey(move_d, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
