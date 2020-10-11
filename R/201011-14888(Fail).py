def go(n, num, buho, index, ans):
	if buho[0]==0 and buho[1]==0 and buho[2]==0 and buho[3]==0: #possible
		
		return ans##
	
	if index == n: #impossible
		return
		
		
	for i in range(len(buho)):
		if i > 0:
			if i == 0:
				buho[0] -= 1
				break
			elif i == 1:
				buho[1] -= 1
				break
			elif i == 2:
				buho[2] -= 1
				break
			elif i == 3:
				buho[3] -= 1
				break

	if i == 0:
		ans = go(n, num, buho, index+1, ans+num[index])
	elif i == 1:
		ans = go(n, num, buho, index+1, ans-num[index])
	elif i == 2:
		ans = go(n, num, buho, index+1, ans*num[index])
	elif i == 3:
		ans = go(n, num, buho, index+1, int(ans/num[index]))
			
	ans = go(n, num, buho, index, ans)



n = int(input())
num = list(map(int, input().split()))
buho = list(map(int, input().split()))

go(n, num, buho, 1, [num[0], num[0]])
