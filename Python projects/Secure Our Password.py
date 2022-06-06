
"""
Create a python program to secure an existing password by replacing a set of characters with th ecorresponding "password-secure" character (provided as tuple).
Example : 
 		Secure = (('s' , '$') ,('and ' ,'&'), ('a' ,'@') , ('o' ,'0'), ('i' ,'1'), ('I','|'))
 		Input: 
 		password = "indians123'
 		output :
 			Your Secure password is |nd1@n$123
 """
Secure = (('s', '$') ,('and ', '&'), ('a', '@') , ('o', '0'), ('i', '1'),('I', '|'))
def securepassword(password):
	for a,b in Secure:
		password = password.replace(a,b)
	return password
if __name__ == "__main__":
	password = input("Enter Your Password :-")
	password = securepassword(password)
	print(f"Your Secure Password is {password}")