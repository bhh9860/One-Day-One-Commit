a = int(input())
b = list(map(int, input().split()))
k = b.copy()
for i in range(len(b)-1, 0, -1):
	if b[i] > b[i-1]:
		c = []
		for j in b[i:]:
			if b[i-1] < j:
				c.append(j)
		c.sort()
		d = c[0]; b[b.index(c[0])] = b[i-1]; b[i-1] = d
		b[i:] = sorted(b[i:])
		break
if k == b:
	print(-1)
else:
	[print(i, end=' ') for i in b]
