while True:
	a = int(input())
	if a == 0:
		break
	else:
		a = list(map(int, str(a)))
		ans = 0
		for i in a:
			if i == 1:
				ans += 2
			elif i == 0:
				ans += 4
			else:
				ans += 3
			ans += 1
	print(ans+1)
