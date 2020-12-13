n = int(input())
time = [list(map(int, input().split())) for i in range(n)]
'''
for i in range(n):
	time[i].append(time[i][1]-time[i][0])'''
time = sorted(time, key = lambda time: (time[1], time[0]))


a = 0
count = 0
index = -1
b = []
while True:
	tempor = []
	
	for i in range(index+1, n):
		if a <= time[i][0]:
			tempor.append(time[i])
		
	a = min(tempor, key=lambda tempor: tempor[1])[1]
	index = tempor.index(min(tempor, key=lambda tempor: tempor[1]))
	b.append(tempor[index])
	count += 1
	print(tempor)
	
	if a >= max(time, key=lambda time: time[1])[1]:
		break
	
if count == 0 and len(time) >= 1:
	count += 1
	
print(count)
