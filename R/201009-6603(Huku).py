def go(s, ans, i):
	if ans.count(',') == 6:
		
		print(' '.join(ans.split(',')))
		return
	if len(s) == i:
		return
		
	go(s, ans+s[i]+',', i+1)
	go(s, ans, i+1)
	return

while True:
	n, *s = list(map(str, input().split()))
	if n == '0':
		break
	go(s, '', 0)
	print()
