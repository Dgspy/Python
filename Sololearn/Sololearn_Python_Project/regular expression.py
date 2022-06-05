
import re
pattern = r"Girish"
if re.match(pattern,"GirishGirishGirish"):
   print("match")
else:
   print("No match")

import re
pattern = r"pam"
match = re.search(pattern,
"eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end()) 
   print(match.span())
   
import re 
pattern = r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]"
email = "girishunde15@gmail.com"
print(re.match(pattern,email))

import re 
pattern = r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]"
email = "girishunde143@gmail.com"
print(re.match(pattern,email))

import re
pattern = r"7558407284"
no = "[7558407284]"
no1 = "[7499605365]"
print(re.search(pattern,no))
if pattern==no:
  print("it is airtel sim no")
elif pattern == no1:
  print("it is not my no")
else:
  print("it is jio sim no",no1)
