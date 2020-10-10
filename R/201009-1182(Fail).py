def go(n, count, ans):
	if n == 1:
		if ans > count:
			ans = count
		return ans
	if n < 1:
		return 
		
	if n % 3 == 0:
		ans = go(n//3, count+1, ans)
	if n % 2 == 0:
		ans = go(n//2, count+1, ans)
	ans = go(n-1, count+1, ans)
	
	return ans
	
n = int(input())
print(go(n, 0, 9999999))
