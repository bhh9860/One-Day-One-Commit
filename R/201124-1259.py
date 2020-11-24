while True:
	a = list(input())
	if a == ['0']:
		break
	b = a.copy()
	b.reverse()
	if a == b:
		print('yes')
	else:
		print('no')
