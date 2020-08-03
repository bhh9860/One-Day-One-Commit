def bun(num): #분해함수
	a = list(str(num)) 
	a.append(num)
	a = list(map(int, a)) 
	return sum(a)
'''a = sum(map(int, str(num)))
	 return a + num 로 대체가능.'''
	
a = int(input())
if a < 10:
	print('0') #한자릿수는 자기자신이 생성자가 될 수 없다.
else:
	b = 0
	for i in range(1, a+1):
		if a == bun(i):
			print(i)
			b += 1
			break
	if b != 1: #b가 1이 아니면 생성자가 없음.
		print('0')
