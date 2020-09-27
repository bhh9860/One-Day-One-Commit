def go(a, index, lotto):
	if len(lotto) == 6:
		print(' '.join(map(str, lotto)))
		return
	if index == len(a):
		return
	go(a, index+1, lotto+[a[index]])
	go(a, index+1, lotto)
	
while True:
	a, *b = list(map(int, input().split()))
	if a == 0:
		break
	go(b, 0, [])
	print('')
