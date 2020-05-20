a = input().split(' ')
b = int(''.join(list(a[0])[::-1]))
c = int(''.join(list(a[1])[::-1]))
if b>c:
	print(b)
else:
	print(c)
