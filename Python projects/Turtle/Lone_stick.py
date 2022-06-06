import turtle
#creating turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

turtle.pensize(1)
# To desogn curve
def curve():
	for i in range(200):
		t.right(1)
		t.forward(2)
t.speed(3)
t.color("pink","red")
	
t.begin_fill()
t.left(150)
t.forward(261.65)
curve()
t.left(129)
curve()
t.forward(561.65)
def curvee():
	for i in range(200):
		t.left(1)
		t.forward(2)
t.forward(261.65)
t.left(129)
curvee()
t.end_fill()
t.hideturtle()
turtle.mainloop()