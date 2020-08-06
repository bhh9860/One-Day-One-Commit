a = ' '.join(input()).split()
ikura = 0

for i in a:
	if i == '1':
		ikura += 500
	elif i == '2':
		ikura += 800
	elif i == '3':
		ikura += 1000
		
print(5000-ikura)
