import itertools

def plus(llist):
	llist = list(map(int, llist))
	box = 0
	for i in range(len(llist)-1):
		box += abs(llist[i] - llist[i+1])
	return box

a = int(input())
b = list(map(str, input().split()))
c = list(itertools.permutations(b))
c = [list(c[i]) for i in range(len(c))]

compair = plus(c[0])
for i in range(1, len(c)):
	if compair < plus(c[i]):
		compair = plus(c[i])

print(compair)
