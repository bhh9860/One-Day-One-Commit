a, b = list(map(int, input().split()))
if b == 1 or b == 2:
	print('NEWBIE!')
elif a < b:
	print('TLE!')
else:
	print('OLDBIE!')
