for z in range(int(input())):
	x = int(input())+1
	y = int(input())
	a = []
	for i in range(y):
		a.append(i+1)
		
	for j in range(x-1):
		for k in range(y):
			a.append(sum(a[0:k+1]))
		del a[0:y]
	print(a.pop())
