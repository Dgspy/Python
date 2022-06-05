
import re
pattern = r"gr.y"
if re.match(pattern, "grey"):
   print("match 1")
if re.match(pattern, "grey"):
   print("match 2")  
if re.match(pattern, "grey"):
   print("match 3")
print("")
import re
pattern = r"[aeiou]"
if re.match(pattern, "grey"):
   print("match 1")
if re.match(pattern, "qwertyuiop"):
   print("match 2")
if re.match(pattern, "rhythm myths"):
   print("match 3")
print("")
import re
pattern = r"[A-Z] [A-Z] [0-9]"
if re.match(pattern, "Ls8"):
   print("match 1")
if re.match(pattern, "E3"):
   print("match 2")
if re.match(pattern, "1ab"):
   print("match 3")
print("")
import re
pattern = r"[^A-Z]"
if re.match(pattern, "this is all quiet"):
   print("match 1")
if re.match(pattern, "AbAdEfG123"):
   print("match 2")
if re.match(pattern, "THISISALLSHOUTING"):
   print("match 3")
print("")
import re
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
   print("match 1")
if re.match(pattern, "eggspamspamegg"):
   print("match 2")
if re.match(pattern, "spam"):
   print("match 3")
print("")   
import re
pattern = r"g+"
if re.match(pattern, "g"):
   print("match 1")
if re.match(pattern, "ggggg14"):
   print("match 2")
if re.match(pattern, "abc"):
   print("match 3")
print("")
import re
pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
   print("match 1")
if re.match(pattern, "icecream"):
   print("match 2")
if re.match(pattern, "sausages"):
   print("match 3")
if re.match(pattern, "ice--cream"):
   print("match 4")
print("")
import re
pattern = r"9{1,3}$"
if re.match(pattern, "9"):
   print("match 1")
if re.match(pattern, "999"):
   print("match 2")   
if re.match(pattern, "9999"):
   print("match 3")
print("")
import re
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern,
"abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())
print("")
import re
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())
print("")
import re
pattern = r"(\D+\d)"
match = re.match(pattern, "hii 999")
if match:
   print("match 1")
match = re.match(pattern, "1,23,456!")
if match:
   print("match 2")
match = re.match(pattern, "! $?")
if match:
   print("match 3")
print("")
import re
pattern = r"\b(cat)\b"
match = re.match(pattern, "the cat sat!")
if match:
   print("match 1")
match = re.match(pattern, "we s>cat<tered?")
if match:
   print("match 2")
match = re.match(pattern, "we scattered.")
if match:
   print("match 3")
print("")
import re
pattern = r"([\w\.-]+)@([\w\.-]+)(\
.[w\.]+)"
str = "please contact info@sololearn.com for assistance"
match = re.search(pattern, str)
if match:
   print(match.group())
print("")
import re
pattern = r"Girish"
if re.match(pattern,"GirishGirishGirish"):
   print("match")
else:
   print("No match")
print("")
import re
pattern = r"pam"
match = re.search(pattern,
"eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end()) 
   print(match.span())
print("")
import re 
pattern = r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]"
email = "girishunde15@gmail.com"
print(re.match(pattern,email))
print("")
import re 
pattern = r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]"
email = "girishunde143@gmail.com"
print(re.match(pattern,email))
print("")
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
