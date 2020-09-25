# 다음 순열 구하는 함수
def next(a):
	for i in range(len(a)-1, 0, -1):
		if a[i-1] < a[i]:
			compare = [max(a)+1, 0]
			for j in range(i, len(a)):
				if a[i-1] < a[j]:
					if compare[0] > a[j]:
						compare[0] = a[j]
						compare[1] = j
			b = compare[0]; a[compare[1]] = a[i-1]; a[i-1] = b
			a[i:] = sorted(a[i:])
			return a
# 다음 순열이 없을 때까지			
while True:
	nani = list(map(int, input().split()))
	if nani[0] == 0: # 0이면 끝
		break
	else:
		ikutsu = nani.pop(0)
		onezero = [0]*(ikutsu-6)+[1]*6 #ex)7 1 2 3 4 5 6 7 -> 0 1 1 1 1 1 1
		sibal = []
		sibal.append(nani[ikutsu-6:]) # 어차피 처음에는 0 1 1 1 1 1 1의 인덱스. 그 다음 순열부터는 다음 와일문.
		
		while next(onezero): # onezero 다음순열이 없을 때까지
			ans = []
			for i in range(ikutsu): # onezero순열을 다 돌리기 위해
				if onezero[i] == 1: # 돌리는 도중 1이 있따면
					ans.append(nani[i])
			sibal.append(ans)
		
		for i in sorted(sibal):
			[print(j, end=' ') for j in i]
			print()
	print() # 문제에 한 케이스 입력할 때마다 한 칸씩 띄라고 해서..
