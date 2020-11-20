for _ in range(int(input())):
	value = []
	name = []
	for i in range(int(input())):
		a = list(input().split())
		value.append(a[0])
		name.append(a[1])
	value = list(map(int, value))
	print(name[value.index(max(value))])
