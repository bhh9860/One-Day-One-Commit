def go(b, ans, i):
	if len(ans) == 6:
		print(' '.join(list(map(str, ans))))
		return
	if len(b) <= i:
		return
	go(b, ans+[b[i]], i+1)
	go(b, ans, i+1)

	
a, *b = list(map(int, input().split()))
while a != 0:
	go(b, [], 0)
	a, *b = list(map(int, input().split()))
	print('')
