H = []

for i in range(9):
	H.append(int(input()))
	
for i in range(9):
	b = H.pop(0) #
	for j in range(8):
		c = H.pop(0)
		if sum(H) == 100:
			break
		else:
			H.append(c)
	if sum(H) != 100:
		H.append(b)
	else:
		for i in sorted(H):
			print(i)
		break
