num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
n = input()
have = []
count = 0

for i in n:
	if i in have:
		del have[have.index(i)]
		
	else:
		if i == '9':
			if '6' in have:
				del have[have.index('6')]	
			else:
				have += num
				count += 1
				del have[have.index(i)]
				
		elif i == '6':
			if '9' in have:
				del have[have.index('9')]
			else:
				have += num
				count += 1
				del have[have.index(i)]
				
		else:
			have += num
			count += 1
			del have[have.index(i)]

print(count)
