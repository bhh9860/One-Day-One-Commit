from itertools import combinations
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
num = list(map(str, num))
l = []
a = list(map(' '.join, combinations(num, 3))) #i개의 원소의 수 만큼의 경우의 수
for j in range(len(a)):
	c = sum(list(map(int, a[j].split(' '))))
	l.append(c)
	
l.sort()
for i in range(len(l)):
	if l[i] > m:
		l = l[0:i]
		break
		
print(l.pop())
