n, k = list(map(int, input().split()))
for _ in range(n):
	a = []
	b = list(input().split())
	for i in range(len(b)):
		a += b[i]*k
	for j in range(k):
		[print(i, end=' ') for i in a]
		print()
