def one(n, count, dp):
	if n == 1:
		return count
	if dp[n] != -1:
		return count
	
	
	if n % 3 == 0:
		a = one(n//3, count+1, dp)
		dp[n] = a
			
	if n % 2 == 0:
		a = one(n//2, count+1, dp)
		dp[n] = a
	
	a = one(n-1, count+1, dp)
	dp[n] = a

	return dp[0:10]


dp = [-1]*1000000
dp[0] = 0
