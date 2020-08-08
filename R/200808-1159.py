#받아서 제일 앞글자만 추가
a = []
for _ in range(int(input())):
	a.append(input()[0])
a.sort()

#축구팀을 이룰 수 있는 알파벳은 b로
b = ''
while(len(a) != 0):
	if a.count(a[0]) >= 5:
		b += a[0]
		del a[:a.count(a[0])]
	else:
		del a[:a.count(a[0])]
	
if b == '':
	print('PREDAJA')
else:
	print(b)
