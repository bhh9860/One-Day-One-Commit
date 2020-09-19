asdf = int(input())
a = list(map(int, input().split()))
b = []
[b.append(i) for i in range(len(a))]
def per(b):
	for i in range(len(b)-1, 0, -1):
		if b[i] > b[i-1]:
			c = []
			for j in b[i:]:
				if b[i-1] < j:
					c.append(j)
			c.sort()
			d = c[0]; b[b.index(c[0])] = b[i-1]; b[i-1] = d
			b[i:] = sorted(b[i:])
			return b
ans = 0
for i in range(len(a)-1):
	ans += a[b[i]]-a[b[i+1]]
	
while per(b):
	k = 0
	for i in range(len(a)-1):
		k += abs(a[b[i]]-a[b[i+1]])
	if k > ans:
		ans = k
		
print(ans)
