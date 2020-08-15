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
	sosu = sosu[2:] #여기까지 2부터 a까지 소수 구하기
	
	if a // 2 in sosu: #6(3,3)이나 22(11,11)같은거
		print(a//2, a//2)
	else:
		k = 1000000 #이건 그냥 높게 잡음
		for i in range(len(sosu)): #소수 한개씩 검사하면서 나아감
			if a-sosu[i] in sosu:
				sosu1 = sosu[i]
				sosu2 = a-sosu1
				sosu3 = abs(sosu1-sosu2)
				if k > sosu3: #한개씩 검사하면서 나아가다가
					k = sosu3
				elif k <= sosu3: #대칭이 되는 가운데를 찾는순간 break
					break
		
		if sosu1 > sosu2: #작은 수부터 출력
			print(sosu2, sosu1)
		else:
			print(sosu1, sosu2)
#
