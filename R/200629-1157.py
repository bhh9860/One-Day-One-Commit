a = list(input().upper())
alpha = []
count = []
for i in range(len(a)): #받은 문자열 a를 하나씩 검사, 있으면 카운트+1 없으면 추가 뒤 카운트 +1
	if a[i] not in alpha:
		alpha.append(a[i])
		count.append(1)
	else:
		count[alpha.index(a[i])] += 1
		
m = sorted(count)
m.reverse()

if len(m) == 1 or m[0] != m[1]:
	print(alpha[count.index(max(count))])
elif m[0] == m[1]:
	print('?')
