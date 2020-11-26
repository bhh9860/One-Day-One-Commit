for _ in range(int(input())):
	ans = 0
	a = list(map(int, input().split()))
	a[1:] = reversed(a[1:])
	for i in range(a.pop(0)-1):
		for j in range(i+1, len(a)):
			x = a[i]
			y = a[j]
			while y != 0:
				n = x % y
				x = y
				y = n
			ans += x
	print(ans)
