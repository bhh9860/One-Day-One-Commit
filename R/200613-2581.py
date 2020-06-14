import math
n = int(input())
m = int(input())
count = 0
sosu = []
for i in range(n, m+1):
	for j in range(2, int(math.sqrt(i))+1):
		if i % j == 0:
			count += 1
		else:
			pass
	if count == 0:
		sosu.append(i)
	count = 0

if 1 in sosu:
	del sosu[0]

if len(sosu) != 0:	
	print(sum(sosu))
	print(min(sosu))
else:
	print(-1)
