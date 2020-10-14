def go(n, count):
	if n == 1:
		return count
	if n < 1:
		return
	
	count = 0
	ans = 9999999999
	
	if n % 3 == 0:
		a = go(n//3, count+1)
		if ans > a:
			ans = a
	
	if n % 2 == 0:
		a = go(n//2, count+1)
		if ans > a:
			ans = a
	
	a = go(n-1, count+1)
	if ans > a:
		ans = a
	
	
	return ans
	
print(go(int(input()), 0))
