si, bun = list(map(int, input().split()))
plus = int(input())
bun += plus
if bun > 59:
	a = bun // 60
	bun %= 60
	si += a
if si > 23:
	si %= 24
print('{0} {1}'.format(si, bun))
