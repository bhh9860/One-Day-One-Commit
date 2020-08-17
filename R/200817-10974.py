a = int(input())
b = [i for i in range(1, a+1)]
copy = b
[print(i, end = ' ') for i in b]
print('')
while copy != sorted(b, reverse = True): # b가 끝순열까지 가면 더이상 반복할 필요 없음
	for i in range(a-1, 0, -1):
		if b[i] > b[i-1]:
			c = []
			for j in b[i:]:
				if b[i-1] < j:
					c.append(j)
			c.sort()
			j = c[0]
			k = b[b.index(j)]; b[b.index(j)] = b[i-1]; b[i-1] = k
			b[i:] = sorted(b[i:])
			[print(i, end = ' ') for i in b]
			print('')
			break
