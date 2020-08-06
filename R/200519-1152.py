a = list(input())
count = 0


if a != [' ']:
	if a[0] == ' ':
		del a[0]
	if a[-1] == ' ':
		del a[-1]
	count += a.count(' ')+1

elif a == [' ']:
	pass

print(count)

#a = print(len(input().split()))
