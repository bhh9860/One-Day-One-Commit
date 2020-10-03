def go(sum, goal):
	if sum > goal:
		return 0
	if sum == goal:
		return 1
	ans = 0
	for i in range(1, 4):
		ans += go(sum+i, goal)
	
	return ans
