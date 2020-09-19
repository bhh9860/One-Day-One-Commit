a = int(input())
c = []
[c.append(list(map(int, input().split()))) for _ in range(a)]
b = []
[b.append(i) for i in range(a)]

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

copy = b.copy()
copy.insert(len(copy), copy.pop(0))
ans = 0
for i in range(a):
	if c[i][copy[i]] != 0:
		ans += c[i][copy[i]]
	else:
		ans = 0
		break
		
while per(b):
	copy = b.copy()
	copy.insert(len(copy), copy.pop(0))
	sibal = 0
	for i in range(a):
		if c[i][copy[i]] != 0:
			sibal += c[i][copy[i]]
		else:
			sibal = 0
			break
	if sibal != 0:
		if sibal < ans:
			ans = sibal
		

print(ans)
