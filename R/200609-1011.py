for i in range(int(input())):
	x, y = map(int, input().split())
	x = y-x
	i = 0
	j = 1
	count = 0
	while (i <= x):
		i += j
		count += 1
		if i < x:
			i += j
			count += 1
			j += 1
			if i < x:
				pass
			else:
				break
		else:
			break
	print(count)
