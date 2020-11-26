for i in range(int(input())):
	a, b = list(map(int, input().split()))
	if a < b:
		a, b = b, a
	c, d = a, b
	while b != 0:
		n = a % b
		a = b
		b = n
	
	print(c*d//a)
