import os

def isgirish(filename):
	with open(filename, "r") as f:
		fileContent = f.read()
	#Detect all forms of girish like GirisH
	if "girish" in fileContent.lower():
		return True
	else:
		return False
if __name__ == "__main__":
	#Listing the contents of this folder
	dir_contents = os.listdir()
	nGirish = 0
	# For each text file ,run is Firish for them 
	for item in dir_contents:
		if item.endswitch("txt"):
			print(f"Detecting Girish in {item}")
			flag = isgirish(item)
			if(flag):
				print(f"******** Girish found in {txt} !!!!!!!!!!")
				nGirish += 1
			else:
				print(f"Girish not found in {item}")
print("@@@@@Girish Detector Summary$$$¢$$$")
print(f"{nGirish} files found with Girish hidden into the txt")