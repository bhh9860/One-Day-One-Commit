n, m = list(map(int, input().split()))
a = []
for _ in range(n):
	a.append(input())

for i in range(m-1, -1, -1):
	ans = str()
	for j in range(n):
		if a[j][i] == '-':
			ans += '|'
		elif a[j][i] == '|':
			ans += '-'
		elif a[j][i] == '/':
			ans += '\\'
		elif a[j][i] == '\\':
			ans += '/'
		elif a[j][i] == '^':
			ans += '<'
		elif a[j][i] == '<':
			ans += 'v'
		elif a[j][i] == 'v':
			ans += '>'
		elif a[j][i] == '>':
			ans += '^'
		else:
			ans += a[j][i]
	print(ans)
