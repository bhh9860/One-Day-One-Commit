def one(n):
	if n == 1:
		return 0
	if d[n] > 0:
		return d[n]
	
	d[n] = one(n-1) + 1
	
	if n % 2 == 0:
		tamp = one(n//2) + 1
		if d[n] > tamp:
			d[n] = tamp
	
	if n % 3 == 0:
		tamp = one(n//3) + 1
		if d[n] > tamp:
			d[n] = tamp
	
	return d[n]

d = [-1] * 1000001
print(one(int(input())))
