def go(ima, goal):
	if goal < ima:
		return 0
	if goal == ima:
		return 1
	now = 0
	for i in range(1, 4):
		now += go(ima+i, goal)
	return now
	
for i in range(int(input())):
	print(go(0, int(input())))
