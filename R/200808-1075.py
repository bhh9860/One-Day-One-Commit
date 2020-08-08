a = list(input())
b = int(input())
a[len(a)-2:] = '00'
a = int(''.join(map(str, a)))
count = 0

for i in range(100):
	if a % b != 0:
		count += 1
		a += 1
	else:
		break

if count < 10:
	count = '0'+str(count)
	
print(count)
