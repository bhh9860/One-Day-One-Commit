a, b, c = list(map(int, input().split()))
d = a*b
d -= c
if d>0:
	print(d)
else:
	print('0')
