for i in range(3):
	a = 0
	for j in range(int(input())):
		a += int(input())
	if a == 0:
		print('0')
	elif a > 0:
		print('+')
	elif a < 0:
		print('-')
