def check(ans):
	count = 0
	for i in ['a', 'e', 'o', 'i', 'u']:
		if i in ans:
			count += 1
	if count >= 1 and len(ans)-count >= 2:
		return 1

def amho(l, m, i, ans):
	if len(ans) == l:
		if check(ans) == 1:
			print(ans)
		return ans
		
	if i == len(m):
		return 0

	amho(l, m, i+1, ans+m[i])
	amho(l, m, i+1, ans)

 

l, c = list(map(int, input().split()))
m = input().split()
m.sort()
m = ''.join(m)

amho(l, m, 0, '')
