def sosu(n): #소수 판별 (범위 : n ~ 2*n)
	m = n*2
	sieve = [True] * (m+1)
	k = int(m ** 0.5)
	for i in range(2, k+1):
		if sieve[i] == True:
			for j in range(i+i, m+1, i):
				sieve[j] = False
	
	count = 0
	if n < 2: #이 코드는 다시 보니까 필요없긴 함 0이면 break됨
		n = 1
	for i in sieve[n+1:]: #true == 소수
		if i == True:
			count += 1
		
	return count
	
while(1):
	a = int(input())
	if a == 0:
		break
	else:
		print(sosu(a))
