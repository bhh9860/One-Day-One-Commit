a = int(input())
cookie = []
for _ in range(a):
	cookie.append(list(input()))

#head
for i in range(a):
	if cookie[i].count('*') == 1:
		head_x = cookie[i].index('*')
		head_y = i
		break
		
#heart
heart_x = head_x
heart_y = head_y + 1

#arm_left
arm_left = heart_x - cookie[heart_y].index('*')
#arm_right
cookie[heart_y][cookie[heart_y].index('*'):heart_x] = '_'*arm_left
arm_right = cookie[heart_y].count('*')-1

#waist
imsi = heart_y
waist = 0
while True:
	imsi += 1
	if cookie[imsi].count('*') == 2:
		break
	else:
		waist += 1

#leg
left_leg = 0
right_leg = 0
imsi_1 = 0
while True:
	if a == imsi:
		break
	if cookie[imsi].count('*') == 2:
		left_leg += 1
		right_leg += 1
		imsi += 1
	elif cookie[imsi].count('*') == 1:
		imsi_1 += 1
		imsi_1_x = cookie[imsi].index('*')
		imsi += 1
	else:
		break
try:	
	if imsi_1_x > heart_x:
		right_leg += imsi_1
	elif imsi_1_x < heart_x:
		left_leg += imsi_1
except:
	pass

print(heart_y+1, heart_x+1)
print(arm_left, arm_right, waist, left_leg, right_leg)
