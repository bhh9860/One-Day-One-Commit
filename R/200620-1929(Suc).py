#https://ko.m.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
n, m = map(int, input().split())
sieve = [True] * (m+1) #리스트는 1부터가 아닌 0부터기 떄문에 m+1
k = int(m ** 0.5) #int(sqrt(m))
for i in range(2, k+1):
	if sieve[i] == True: 
		for j in range(i+i, m+1, i): #i의 배수는 소수가 아니기 때문에 모두 소수처리 예)2는 소수, 4, 6, 8....은 낫소수
			sieve[j] = False
	
sieve = sieve[n:] #n부터니까 슬라이싱

if n == 0:
	n = 2
	sieve = sieve[2:]
elif n == 1:
	n = 2
	sieve = sieve[1:]

for i in range(len(sieve)):
	if sieve[i] == True:
		print(n)
	n += 1
