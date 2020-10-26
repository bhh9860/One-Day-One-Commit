def fibo(n, dp):
	if n == 0:
		dp[0] += 1
		return 0
	if n == 1:
		dp[1] += 1
		return 1
	
	if dp[n] != -1: #DP
		return dp[n]
		
	dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
	return dp[n]
		

for _ in range(int(input())):
	n = int(input())
	dp = [-1]*(n+3) #몇 백만개씩 만들면 시간초과남
	#0, 1, 2일 때는 직접 출력.
	if n == 0:
		print(1, 0)
		continue
	elif n == 1:
		print(0, 1)
		continue
	elif n == 2:
		print(1, 1)
		continue
	fibo(n, dp)
	print(dp[n-1], dp[n])
