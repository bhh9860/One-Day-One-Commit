while(1):
	a, b, c = map(int, input().split())
	if a == 0 & b == 0 & c == 0:
		break
	else:
		num = [a, b, c]
		num.sort()
		if num[0]**2 + num[1]**2 == num[2]**2:
			print('right')
		else:
			print('wrong')
