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

def amho(l, passwordhubo, password, i):
	if len(password) > l:
		return
	if len(passwordhubo) <= i:
		return
	if len(password) == l:
		if check(password) == 1:
			print(password)
			return
	amho(l, passwordhubo, password+passwordhubo[i], i+1)
	amho(l, passwordhubo, password, i+1)

passwordhubo.append('zz')
amho(l, passwordhubo, '', 0)
