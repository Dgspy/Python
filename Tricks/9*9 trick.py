a = []
for i in range(10):
	a.append(i * ++i)
for a[i] in a:
	print(a[i])
"""
answer is ::
0
1
4
9
16
25
36
49
64
64 why 9*9 is 64
[Program finished]"""