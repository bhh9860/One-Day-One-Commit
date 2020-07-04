for z in range(int(input())):
	a = int(input())
	true = [True] * (a+1)
	for i in range(2, int(a ** 0.5)+1):
		if true[i] == True:
			for j in range(i+i, a+1, i):
				true[j] = False
	
	sosu = []
	for i in range(len(true)):
		if true[i] == True:
			sosu.append(i)
	sosu = sosu[2:]
	
	if a // 2 in sosu:
		print(a//2, a//2)
	else:
		k = 1000000
		for i in range(len(sosu)):
			if a-sosu[i] in sosu:
				sosu1 = sosu[i]
				sosu2 = a-sosu1
				sosu3 = abs(sosu1-sosu2)
				if k > sosu3:
					k = sosu3
				elif k <= sosu3:
					break
		
		if sosu1 > sosu2:
			print(sosu2, sosu1)
		else:
			print(sosu1, sosu2)
