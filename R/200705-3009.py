'''
문제푸는 방법
1. 세 점중 x값이 같은 두 점을 찾는다.
2. 두 점의 y값 중 나머지 한점과의 y값이 다른 점의 y값을 캐치한다.
3. 나머지 한점의 x값과 방금 캐치한 y값이 마지막 한 점의 위치.
'''
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

if a1 == b1:
	if c2 == a2:
		print(c1, b2)
	elif c2 == b2:
		print(c1, a2)
elif b1 == c1:
	if a2 == b2:
		print(a1, c2)
	elif a2 == c2:
		print(a1, b2)
elif c1 == a1:
	if b2 == c2:
		print(b1, a2)
	elif b2 == a2:
		print(b1, c2)
