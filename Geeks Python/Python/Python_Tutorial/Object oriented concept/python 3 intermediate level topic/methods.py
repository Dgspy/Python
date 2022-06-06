class vector2D:
	x = 0.0
	y = 0.0
	def set(self,x,y):
		self.x = x
		self.y = y
def main():
	v = vector2D()
	v.set(5,6)
	print("x:" + str(v.x) + ", y :"+ str(v.y))
if __name__ =='__main__':
	main()