while(True):
	a, b = list(map(list, input().split()))
	count = 0
	if a == ['0'] and b == ['0']:
		break
	else:
		if len(a) < len(b):
			for i in range(len(a)):
				c = int(a.pop())
				d = int(b.pop())
				if c+d > 9:
					count += 1
		elif len(a) >= len(b):
			for i in range(len(b)):
				c = int(a.pop())
				d = int(b.pop())
				if c+d > 9:
					count += 1
	print(count)
