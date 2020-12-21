a = int(input())
b = list(' '*a*2)

for i in range(1, a+1):
	b[0:i] = '*'*i
	b[len(b)-i:] = '*'*i
	print(''.join(b))
	

for i in range(a-1, 0, -1):
	b = list(' '*a*2)
	b[0:i] = '*'*i
	b[len(b)-i:] = '*'*i
	print(''.join(b))
