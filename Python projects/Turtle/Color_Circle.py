import turtle
turtle.bgcolor("black")
turtle.pensize("2")
turtle.speed(0)

for i in range(10):
	for colours in ["red","blue","pink","orange","cyan","yellow","green","skyblue","darkred","darkgreen"]:
		turtle.color(colours)
		turtle.circle(100)
		turtle.left(10)
turtle.hideturtle()
turtle.done()