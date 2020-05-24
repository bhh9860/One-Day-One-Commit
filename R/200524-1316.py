good = 0
sibal = int(input())
for i in range(sibal):
	a = list(input())
	count = 0
	swtich = 0
	while(1):
		try:
			if a[count] == a[count+1]:
				del a[count+1]
			else:
				count += 1
		except:
			break
			
	for j in a:
		if a.count(j) > 1:
			swtich += 1
			break
		else:
			continue
	if swtich == 0:
		good += 1

print(good)
