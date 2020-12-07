a = int(input())
hwak = []
for i in range(a):
	hwak.append(input().split('.')[1])

hwak.sort()

i = 0
hwakcount = []
while True:
	if i == len(hwak):
		break
	print(hwak)
	bcount = hwak.count(hwak[i])
	hwakcount.append(bcount)
	hwak[i:bcount+i] = hwak[i]
	i+=1
