import turtle as t
s = t.Screen()
t.speed(0)
t.tracer(20)
t.width(3)
t.setup(1537.865)
t.bgcolor("black")
color = ("red","green" ,"orange","blue","cyan","yellow")
for i in range(1450):
	t.pencolor("black")
	t.fillcolor(color[i%6])
	t.fd(i)
	t.begin_fill()
	t.fd(i)
	t.rt(90)
	t.circle(i,270)
	t.end_fill()
turtle.done()