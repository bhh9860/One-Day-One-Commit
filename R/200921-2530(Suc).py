a = list(map(int, input().split()))
b = int(input())

a[1] += b//60
a[2] += b%60

if a[2] >= 60:
	a[1] += a[2]//60
	a[2] = a[2]%60
if a[1] >= 60:
	a[0] += a[1]//60
	a[1] = a[1]%60
if a[0] >= 24:
	a[0] = a[0]%24

[print(i, end= ' ') for i in a]
