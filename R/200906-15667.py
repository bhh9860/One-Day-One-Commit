a = int(input())
a -= 1
num = 1
while True:
	if num**2 + num == a:
		break
	else:
		num += 1
print(num)
