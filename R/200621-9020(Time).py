import time
for b in range(int(input())):
	a = int(input())
	start = time.time()
	sieve = [True] * (a+1)
	aa = int(a ** 0.5)
	for i in range(2, aa+1):
		if sieve[i] == True:
			for j in range(i+i, a+1, i):
				sieve[j] = False
	
	sosu = []			
	for i in range(len(sieve)):
		if sieve[i] == True:
			sosu.append(i)
	sosu = sosu[2:]
	
	sosuzip = []
	for i in range(len(sosu)):
		namuji = a - sosu[i]
		if namuji in sosu:
			sosuzip.append([sosu[i], namuji])
	
	zulde = []	
	for i in range(len(sosuzip)):
		zulde.append(abs(sosuzip[i][0]-sosuzip[i][1]))
	
	print(sosuzip[zulde.index(min(zulde))][0], sosuzip[zulde.index(min(zulde))][1])
	print('time : ', time.time()-start)
