n, s = list(map(int, input().split()))
sibal = list(map(int, input().split()))

# sibal = 주어진 수열, s = 만들어야 하는 값, i = 인덱스, ima = 더한 현재 값[]
def hap(sibal, s, i, ima):
	#중요! i == len(sibal)이 들어가지 않으면 모든 부분집합을 구할 수 없음.
	#예)2, -2, 2의 집합과 목표값 2가 있을 때 정답은 [2, X, X], [2, -2, 2]가 되어야 하나, 위의 조건이 없으면 [2]에서 sum(ima) == s의 조건으로 바로 return 1이 되어버림.
	if sum(ima) == s and i == len(sibal): #
		if ima == []:
			return 0
		return 1
	if len(sibal) <= i:
		return 0
	
	ans =  0

	ans += hap(sibal, s, i+1, ima+[sibal[i]])
	ans += hap(sibal, s, i+1, ima)
	
	return ans

print(hap(sibal, s, 0, []))
