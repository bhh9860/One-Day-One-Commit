while True:
	a = list(input().upper())
	if a == ['#']:
		break
	else:
		b = ['A', 'I', 'U', 'O', 'E']
		c = 0
		for i in b:
			c += a.count(i)
			
		print(c)
