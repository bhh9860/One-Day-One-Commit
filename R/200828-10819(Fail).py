import math
def next(seq):
	for i in range(len(seq)-1, 0, -1):
		if seq[i-1] < seq[i]:
			big = []
			for j in seq[i:]:
				if seq[i-1] < j:
					big.append(j)
			big.sort()
			a = seq[seq.index(big[0])]; seq[seq.index(big[0])] = seq[i-1]; seq[i-1] = a
			seq[i:] = sorted(seq[i:])
			return seq

def plus(llist):
	llist = list(map(int, llist))
	box = 0
	for i in range(len(llist)-1):
		box += abs(llist[i] - llist[i+1])
	return box
	
sibal = input()
a = list(input().split())
a.sort()
b = list(reversed(a))

compair = plus(a)
for _ in range(math.factorial(len(a))):
	next(a)
	if compair < plus(a):
		compair = plus(a)
print(compair)
