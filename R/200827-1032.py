a = int(input())
mozi = []
ans = []
for _ in range(a):
	mozi.append(input())
	
if len(mozi) == 1:
	print(mozi[0])
else:
	for i in range(len(mozi[0])):
		b = 0
		for j in range(a-1):
			if mozi[j][i] != mozi[j+1][i]:
				b = 1
		if b == 0:
			ans.append(mozi[j][i])
		elif b == 1:
			ans.append('?')
	
print(''.join(ans))
