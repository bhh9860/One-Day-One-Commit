n = int(input())
hwak = {}
for i in range(n):
	a = input().split('.')[1]
	if a not in hwak:
		hwak[a] = 1
	else:
		hwak[a] += 1

b = sorted(hwak.items())
for j in b:
	print(list(j)[0], list(j)[1])
