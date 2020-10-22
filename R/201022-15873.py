a = list(input())
if len(a) == 2:
	print(int(a[0])+int(a[1]))
elif len(a) == 3:
	if a[1] == '0':
		print(int(''.join(a[0:2]))+int(a[2]))
	elif a[2] == '0':
		print(int(a[0])+int(''.join(a[1:])))
elif len(a) == 4:
	print(int(''.join(a[0:2]))+int(''.join(a[2:])))

