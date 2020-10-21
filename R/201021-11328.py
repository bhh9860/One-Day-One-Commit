for _ in range(int(input())):
	a, b = list(map(list, input().split()))
	a.sort()
	b.sort()
	if a == b:
		print('Possible')
	else:
		print('Impossible')
