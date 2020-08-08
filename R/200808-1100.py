a = []
for i in range(8):
	a.append(list(input()))

b = 0

#x가 짝수일때는 y가 짝수, x가 홀수일때는 y가 홀수인 자리
#중에서 'F'라면 b+=1
for i in range(8):
	if i % 2 == 1:
		for j in range(8):
			if j % 2 == 1:
				if a[i][j] == 'F':
					b += 1
	else:
		for k in range(8):
			if k % 2 == 0:
				if a[i][k] == 'F':
					b += 1

print(b)
