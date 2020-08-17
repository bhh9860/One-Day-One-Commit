# 알고리즘 메모 다음 순열 참조
a = int(input())
b = list(map(int, input().split()))
for i in range(len(b)-1, -1, -1): 
	if i == 0: # b는 마지막 순열
		print(-1)
		break
	elif b[i-1] < b[i]:
		big = []
		for j in range(i, len(b)):
			if b[i-1] < b[j]: # 방법 1
				big.append(b[j]) # 방법 1
		big.sort() # 방법 2 - j = big[0] 
		c = b[b.index(big[0])]; b[b.index(big[0])] = b[i-1]; b[i-1] = c # 방법 3
		b[i:] = sorted(b[i:]) # 방법 4
		[print(i, end=' ') for i in b]
		break
