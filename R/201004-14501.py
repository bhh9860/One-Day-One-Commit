def go(n, t, p, index, ima):
	if index == n:
		return ima
	
	if index > n:
		return 0
			
	ans = 0
	a = go(n, t, p, index+t[index], ima+p[index])
	if ans < a:
		ans = a
	a = go(n, t, p, index+1, ima)
	if ans < a:
		ans = a
	
	return ans

n = int(input())
t = []
p = []
for _ in range(n):
	a, b = list(map(int, input().split()))
	t.append(a)
	p.append(b)

print(go(n, t, p, 0, 0))
