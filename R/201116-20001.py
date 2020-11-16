count = 0
if input() == '고무오리 디버깅 시작':
	while True:
		a = input()
		if a == '고무오리 디버깅 끝':
			break
		else:
			if count > 0:
				if a == '문제':
					count += 1
				elif a == '고무오리':
					count -= 1
			elif count == 0:
				if a == '문제':
					count += 1
				elif a == '고무오리':
					count += 2

if count == 0:
	print('고무오리야 사랑해')
else:
	print('힝구')
