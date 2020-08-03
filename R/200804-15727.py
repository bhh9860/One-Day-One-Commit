a = int(input())
b = 0
while a != 0:
	if a >= 5:
		a -= 5
		b += 1
	else:
		b += 1
		break
print(b)

#print(int((int(input()) - 0.5) // 5 + 1))로 한번에 가능
