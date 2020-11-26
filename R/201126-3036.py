n = int(input())
a, *b = map(int, input().split())
for i in b:
	num0 = a
	num = a
	num1 = i
	while num1 != 0:
		n = num % num1
		num = num1
		num1 = n
	print(str(num0//num)+'/'+str(i//num))
