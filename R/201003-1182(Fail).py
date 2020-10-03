n, s = list(map(int, input().split()))
sibal = list(map(int, input().split()))

# sibal = 주어진 수열, s = 만들어야 하는 값, i = 인덱스, ima = 더한 현재 값
def hap(sibal, s, i, ima):
	if ima == s:
		return 1
	if len(sibal) <= i:
		return 0
	
	ans = 0
	ans += hap(sibal, s, i+1, ima+sibal[i])
	ans += hap(sibal, s, i+1, ima)
	
	return ans
	
print(hap(sibal, s, 0, 0))
