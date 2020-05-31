a = int(input())
i = 1
j = 1
while (i < a):
	j += 1
	i += j

count = j
j = (i - (j-1))

countt = (a-j) + 1

if count % 2 == 0:
	print("%d/%d" %(countt, (count+1)-countt))
else:
	print("%d/%d" %((count+1)-countt, countt))
