def go(ssum, goal):
	if ssum > goal:
		return 0
	if ssum == goal:
		return 1
	now = 0
	for i in range(1, 4):
		now += go(ssum+i, goal)
	
	return now
	
for i in range(int(input())):
	print(go(0, int(input())))
