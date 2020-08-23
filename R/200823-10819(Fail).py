def hap(listt):
	k = 0
	for i in range(len(listt)-1):
		k += abs(listt[i] - listt[i+1])
	return k

a = int(input())
b = sorted(list(map(int, input().split())))
b_copy = b
c = []
c.append(hap(b))
while b_copy != sorted(b, reverse=True):
	for i in range(a-1, 0, -1): #0made?
		if b_copy[i] > b_copy[i-1]:
			b_copy_big = []
			for j in b_copy[i:]:
				if b_copy[i-1] < j:
					b_copy_big.append(j)
			b_copy_big.sort()
			swap = b_copy_big[0]; b_copy[b_copy.index(swap)] = b[i-1]; b[i-1] = swap
			b[i:] = sorted(b[i:])
			c.append(hap(b_copy))
			
			break

c.sort()
print(c[-1])

