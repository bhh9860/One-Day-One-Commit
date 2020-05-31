count = 0
alpha = 1
ap = 6 #alpha plus
beta = int(input())
while (alpha < beta):
	alpha += ap
	ap += 6
	count += 1
	
print(count+1)
