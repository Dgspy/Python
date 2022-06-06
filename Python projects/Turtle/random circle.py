import turtle
import random
a = random.randint(0,250)
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
for i in range(a):
	t.color("cyan")
	t.circle(i)
	t.left(5)
turtle.done()