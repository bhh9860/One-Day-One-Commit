a = int(input())
b = []
for i in range(a):
	b.append(int(input()))
b.sort()
[print(i) for i in b]
