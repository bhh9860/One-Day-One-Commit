#.
a = int(input())
def fac(i):
	if i == 1 or i == 0:
		return 1
	return i * fac(i-1)

print(fac(a))
