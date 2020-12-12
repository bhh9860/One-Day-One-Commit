n, k = list(map(int, input().split()))
num = []
[num.append(i) for i in range(1, n+1)]
check = [0]*n

i = -1
ans = []
for _ in range(n):
	for _ in range(k):
		i += 1
		if n <= i:
			i -= n
		while check[i] != 0:
			i += 1
			if n <= i:
				i -= n
	ans.append(num[i])
	check[i] = 1
	
print(' '.join(map(str, ans)))
