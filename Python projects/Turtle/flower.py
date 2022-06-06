import turtle as t

t.bgcolor("yellow")
def flower():
	for i in range(300):
		for colors in ["red","blue","orange","white"]:
			t.pencolor(colors)
			t.circle(190-i,90)
			t.left(90)
			t.speed(0)
			t.circle(190-i,90)
			t.left(18)
flower()
t.mainloop()