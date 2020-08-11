H = []

for i in range(9):
	H.append(int(input()))
	
for i in range(9):
	for j in range(i+1, 9):
		if (sum(H) - H[i] - H[j] == 100):
			del H[i]
			del H[j-1]
			break
	if len(H) == 7:
		break

for i in sorted(H):
	print(i)
