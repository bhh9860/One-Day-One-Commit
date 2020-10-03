l, c = list(map(int, input().split()))
passwordhubo = list(input().split())
passwordhubo.sort()

def check(password):
	za = 0
	mo = 0
	a = ['a', 'i', 'u', 'o', 'e']
	for i in password:
		if i in a:
			mo += 1
		else:
			za += 1
	
	if mo >= 1 and za >= 2:
		return 1
	else:
		return 0

# amho함수의 제일 앞 문단에 각각 두 개의 이프문(1, 2)이 있는데, 이때 순서는 반드시 하단 코드와 같아야 한다.
# 만약 순서가 바뀐다면, 정답인데도 불구하고 2에 의해서 걸러져버린다. 그러나 하단 코드의 순서라면, 일단 체크를 통해서 정답이 프린트 된 뒤(1)에 걸러진다(2).
def amho(l, passwordhubo, password, i):
	if len(password) == l: #1
		if check(password) == 1:
			print(password)
			return
	if len(passwordhubo) <= i: #2
		return
	amho(l, passwordhubo, password+passwordhubo[i], i+1)
	amho(l, passwordhubo, password, i+1)

amho(l, passwordhubo, '', 0)
