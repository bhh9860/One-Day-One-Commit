a = list(map(int, input().split()))
b = int(input())
bun = b // 60
cho = b % 60
a[1] += bun
a[2] += cho

if a[2] > 59:
	a[2] -= 60
	a[1] += 1

if a[1] > 59:
	a[1] -= 60
	a[0] += 1

if a[0] > 23:
	a[0] -= 24
	
print(a[0], a[1], a[2])
