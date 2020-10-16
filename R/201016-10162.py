a = int(input())
b,c,d=0,0,0
while True:
	if a >= 300:
		a-=300
		b+=1
	else:
		break
		
while True:
	if a >= 60:
		a-=60
		c+=1
	else:
		break
		
while True:
	if a >= 10:
		a-=10
		d+=1
	else:
		break
				
if a != 0:
	print(-1)
else:
	print(b,c,d)
