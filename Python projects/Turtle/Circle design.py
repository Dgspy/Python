import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
turtle.bgcolor("black")
h = 0
for i in range(70):
	c = colorsys.hsv_to_rgb(h,1,1)
	t.color(c)
	t.begin_fill()
	t.circle(i,216)
	t.circle(i,-144)
	t.right(100)
	h+=0.006
	t.end_fill()
turtle.done()
