a = int(input())
if a <= 5:
	print(a)
else:
	a -= 5
	b = a%8
	if b == 1 or b == 7:
		print(4)
	elif b == 2 or b == 6:
		print(3)
	elif b == 3 or b == 5:
		print(2)
	elif b == 4:
		print(1)
	elif b == 0:
		print(5)
