def one(n):
	if n == 1:
		return 0
	if d[n] > 0:
		return d[n]
	d[n] = one(n-1) + 1
	if n % 2 == 0:
		temp = one(n//2) + 1
		if d[n] > temp:
			d[n] = temp
	
	if n % 3 == 0:
		temp = one(n//3) + 1
		if d[n] > temp:
			d[n] = temp
	
	return d[n]
n = int(input())	
d = [0] * (n+2)
print(one(n))
