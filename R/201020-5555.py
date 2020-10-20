count = 0
a = input()
for i in range(int(input())):
	b = input()*2
	for j in range(10):
		if b[j:j+len(a)] == a:
			count += 1
			break
print(count)
