for _ in range(int(input())):
	a, b = list(map(int, input().split()))
	c = pow(a, b)
	print(str(c)[-1])
