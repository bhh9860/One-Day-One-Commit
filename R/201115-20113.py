a = int(input())
b = [0] * a
c = list(map(int, input().split()))
for i in c:
	if i == 0:
		continue
	else:
		b[i-1] += 1

if b.count(max(b)) > 1:
	print('skipped')
elif b.count(max(b)) == 1:
	print(b.index(max(b))+1)

