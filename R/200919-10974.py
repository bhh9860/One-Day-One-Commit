a = int(input())
b = []
[b.append(i) for i in range(1, a+1)]
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

[print(i, end=' ') for i in b]
print('')
while per(b):
	[print(i, end=' ') for i in b]
	print('')
