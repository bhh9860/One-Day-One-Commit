for _ in range(int(input())):
	a = list(input())
	b = 0
	if len(a)%2==1: #애초에 홀수면 VPS가 아님.
		print('NO')
	else:
		while(1):
			for i in range(len(a)-1): #첫번째 이프에서 i+1을 검사하기 때문에, len(a)-1이어야만 함. 예시 들어보면 왜 이런지 금방 이해할 수 있음.
				if a[i] == '(' and a[i+1] == ')':
					del a[i+1]
					del a[i]
					if len(a) == 0: #모두 지우고 아무것도 남지 않을 경우. 다시 말해 VPS일 경우.
						b += 1         
					break
				else:
					if i == len(a)-2: #끝까지 검사했지만 첫번째 if조건에 걸리지 않고('()'가 아니고) else에 걸렸기 때문에 VPS가 아님.
						b += 2
						break

			if b == 1:
				print('YES')
				break
			if b == 2:
				print('NO')
				break
