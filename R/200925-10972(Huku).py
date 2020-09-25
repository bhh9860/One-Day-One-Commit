def next(a):
	for i in range(len(a)-1, 0, -1):
		if a[i-1] < a[i]:
			compare = [max(a)+1, 0]
			for j in range(i, len(a)):
				if a[i-1] < a[j]:
					if compare[0] > a[j]:
						compare[0] = a[j]
						compare[1] = j
			b = compare[0]; a[compare[1]] = a[i-1]; a[i-1] = b
			a[i:] = sorted(a[i:])
			return a
			
num = int(input())
what = list(map(int, input().split()))
sibal = what.copy()
next(what)
if what != sibal:
	[print(i, end=' ') for i in what]
else:
	print(-1)
