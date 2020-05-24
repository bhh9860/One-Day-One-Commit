alpha = ['a', 'b', 'e', 'f', 'g', 'h', 'i', 'k', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y']
beta = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = list(input())
count = 0

for i in alpha:
	try:
		while(1):
			del a[a.index(i)]
			count += 1
	except:
		pass

while len(a) > 1:
	if a[0] + a[1] in beta:
		count += 1
		del a[0:2]
		
	elif a[0] + a[1] not in beta:
		if a[0] + a[1] == 'dz':
			try: #a[2] is not NONE
				if a[2] == '=':
					count += 1
					del a[0:3]
				else:
					count += 1
					del a[0]
			except: #a[2] is NONE
				del a[0:2]
				count += 2
		else:
			count += 1
			del a[0]
			
if len(a) == 1:
	count += 1
print(count)
