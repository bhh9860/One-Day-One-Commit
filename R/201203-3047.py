a = list(map(int, input().split()))
b = list(input())
a.sort()
for i in b:
	if i == 'A':
		print(a[0], end = ' ')
	elif i == 'B':
		print(a[1], end = ' ')
	elif i == 'C':
		print(a[2], end = ' ')
