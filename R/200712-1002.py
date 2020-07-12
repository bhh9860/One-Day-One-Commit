#다른 사람 코드를 보니 굳이 r5, r6을 만들 필요는 없었다. 그냥 min, max이용하면 됐었음.
#r5, r6을 만들 때도 굳이 제곱을 했야했나 싶다. 생각없이 막 한듯.

for i in range(int(input())):
	x1, x2, r1, y1, y2, r2 = map(int, input().split())
	guri1 = ((abs(y1-x1) ** 2) + (abs(y2-x2) ** 2)) ** 0.5 #두 원의 중점의 거리
	guri2 = r1 + r2 #두 원의 반지름의 합
	
	#더 긴 반지름이 r5, 짧은 반지름은 r6
	r3 = r1 ** 2
	r4 = r2 ** 2
	if r3 > r4:
		r5 = r1
		r6 = r2
	elif r3 < r4:
		r5 = r2
		r6 = r1
	elif r3 == r4:
		r5 = r1
		r6 = r1
		
	if guri1 < r5:#한 원의 중심이 나머지 한 원의 안에 있을 때
		if (x1, x2, r1) == (y1, y2, r2):
			print(-1)
		elif r5 - r6 < guri1:
			print(2)
		elif r5 - r6 == guri1:
			print(1)
		elif r5 - r6 > guri1:
			print(0)
	
	elif guri1 > r5:#한 원의 중심이 나머지 한 원의 밖에 있을 때
		if guri1 > guri2:
			print(0)
		elif guri1 == guri2:
			print(1)
		elif guri1 < guri2:
			print(2) 
			
	elif guri1 == r5:
		print(2)
