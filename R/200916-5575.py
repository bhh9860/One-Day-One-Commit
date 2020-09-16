for i in range(3):
	time = list(map(int, input().split()))
	c = time[5]-time[2]
	b = time[4]-time[1]
	a = time[3]-time[0]
	if c < 0:
		b -= 1
		c += 60
	
	if b < 0:
		a -= 1
		b += 60
		
	print(a, b, c)
