partA, partB = list(map(int, input().split()))
a = list(input())
a.reverse()
b = list(input())
sec = int(input())

wayA = ['->'] * partA
wayB = ['<-'] * partB

antmove = a+b
waymove = wayA + wayB


for _ in range(sec):
	n = 0
	for i in range(0, partA+partB-1):
		if i+n+1 > partA+partB-1:
			break
		if waymove[i+n] == '->' and waymove[i+1+n] == '<-':
			waymove[i+n], waymove[i+1+n] = waymove[i+1+n], waymove[i+n]
			antmove[i+n], antmove[i+1+n] = antmove[i+1+n], antmove[i+n]
			n += 1
print(''.join(antmove))

