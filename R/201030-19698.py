a, b, c, d = list(map(int, input().split()))
x = b // d
y = c // d
z = x * y
if a > z:
	print(z)
elif a <= z:
	print(a)
