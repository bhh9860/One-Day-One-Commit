def go(n, k, w, v, ans, index):
	if k >= sum(ans) and index == n:
		money = 0
		for i in range(len(ans)):
			money += v[i]
		return money
		
	if k < sum(ans):
		return 0

	a = 0
	b = go(n, k, w, v, ans+[w[index]], index+1)
	if a < b:
		a = b
		
	b = go(n, k, w, v, ans, index+1)
	if a < b:
		a = b
	
	return a







n, k = list(map(int, input().split()))
w = []
v = []
for i in range(n):
	a, b = list(map(int, input().split()))
	w.append(a)
	v.append(b)

print(go(n, k, w, v, [], 0))
