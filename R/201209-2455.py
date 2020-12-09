ima = 0
ans = 0
for i in range(4):
	a, b = list(map(int, input().split()))
	ima -= a
	if ans < ima:
		ans = ima
	ima += b
	if ans < ima:
		ans = ima

print(ans)
