a = input().split()
a = list(map(int, a))
b = 0
for i in a:
	b += i**2

print(b%10)
