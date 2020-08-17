'''
예시 ) 2 4 1 3
1. 제일 뒤(3)를 i로 두고, 앞으로 한칸씩 전진하며 i가 i-1보다 작으면 멈춘다. (i = 1, i-1 = 4)
2. i-1보다 작으면서 가장 큰 수를 [i:]에서 찾는다. 그 수를 j로 둔다. (4보다 작으면서 가장 큰수 = j = 3)
3. i-1과 j를 스왑하고, [i:]을 내림차순정렬한다. (2413 -> (스왑)2314 -> (내림차순)2341)'''

a = int(input())
b = list(map(int, input().split()))
for i in range(a-1, -1, -1): #1
	if i == 0:#오름차순이면 -1출력
		print(-1)
		break
	elif b[i] < b[i-1]: #1
		c = []
		for j in range(i, a): #2
			if b[i-1] > b[j]: #2
				c.append(b[j]) #2
		c.sort(reverse=True) #2
		k = b[b.index(c[0])]; b[b.index(c[0])] = b[i-1]; b[i-1] = k #3
		b[i:] = sorted(b[i:], reverse=True)#3
		[print(i, end=' ') for i in b]
		break
		
		
'''
a = int(input())
b = list(map(int, input().split()))
for i in range(a-1, -1, -1):
	if i == 0:
		print(-1)
		break
	elif b[i] < b[i-1]:
		c = b[i:]
		for j in c:
			if b[i-1] < j:
				del c[c.index(j)]
		c.sort(reverse=True)
		k = b[b.index(c[0])]; b[b.index(c[0])] = b[i-1]; b[i-1] = k
		b[i:] = sorted(b[i:], reverse=True)
		[print(i, end=' ') for i in b]
		break
		왜 이게 안되는지 당최 이해를 할 수가 없음
		'''
