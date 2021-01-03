a = list(input().upper())
b = list('CAMBRIDGE')
for i in b:
	while True:
		if a.count(i) == 0:
			break
		else:
			del a[a.index(i)]
			
print(''.join(a))
