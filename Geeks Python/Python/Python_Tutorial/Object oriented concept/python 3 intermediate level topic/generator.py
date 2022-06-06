'''def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]
def main():
	r = reverse("darkside")
	for i in r:
		print(i)
	data = "darkside"
	print(list(data[i]for i in range(len(date)-1,-1,-1)))
if __name__ == '__main':
	main()
	'''
# A Python program to demonstrate working of Generators
def Reverse(data):
	# this is like counting from 100 to 1 by taking one(-1)
	# step backward.
	for index in range(len(data)-1, -1, -1):
		yield data[index]

def Main():
	rev = Reverse('Harssh')
	for char in rev:
		print(char)
	data ='Harssh'
	print(list(data[i] for i in range(len(data)-1, -1, -1)))

if __name__=="__main__":
	Main()
