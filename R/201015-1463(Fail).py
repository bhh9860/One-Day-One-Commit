def one(n, dp, count):
    if n == 1:
        return count
    if dp[n] != -1:
        return dp[n]
    
    count = 0
    if n % 3 == 0: #1
        a = one(n//3, dp, count+1)
        dp[n] = a
    
    if n % 2 == 0: #2
        a = one(n//2, dp, count+1)
        dp[n] = a
    
    a = one(n-1, dp, count+1) #3
    dp[n] = a
    
    return dp

dp = [-1]*10
dp[0] = 0

print(one(3, dp, 0))
