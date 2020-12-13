n, k = list(map(int, input().split()))
num = [i for i in range(1, n+1)]

count = 0
ans = []

for i in range(n):
	count += k-1
	if count >= len(num):
		count %= len(num)
	
	ans.append(num.pop(count))

ans = list(map(str, ans))
print('<', ', '.join(ans)[:], '>', sep='')
