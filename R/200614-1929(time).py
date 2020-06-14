n, m = map(int, input().split())
sosu = []
notsosu = []
for i in range(n , m+1):
	sosu.append(i)

for i in range(2, m+1):
	for j in range(n, m+1):
		if j % i == 0:
			notsosu.append(j)
		else:
			continue

for i in range(2, m+1):
	if notsosu.count(i) == 1:
		del notsosu[notsosu.index(i)]
		
notsosu = list(set(notsosu))

for i in notsosu:
	del sosu[sosu.index(i)]
if 1 in sosu:
	del sosu[0]
	
for i in sosu:
	print(i)
