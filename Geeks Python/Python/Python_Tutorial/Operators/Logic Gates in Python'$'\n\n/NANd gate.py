# Python3 program to illustrate
# working of NAND gate

def NAND (a, b):

	if a == 1 and b == 1:
		return False
	else:
		return True

# Driver code
if __name__=='__main__':
	print(NAND(1, 1))

	print("+---------------+----------------+")
	print(" | AND Truth Table | Result |")
	print(" A = False, B = False | A AND B =",NAND(False,False)," | ")
	print(" A = False, B = True | A AND B =",NAND(False,True)," | ")
	print(" A = True, B = False | A AND B =",NAND(True,False)," | ")
	print(" A = True, B = True | A AND B =",NAND(True,True)," | ")
