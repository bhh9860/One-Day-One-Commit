ans = 0
for _ in range(int(input())):
	num, apple = list(map(int, input().split()))
	if num > apple:
		ans += apple
	else:
		if apple % num == 0:
			pass
		else:
			a = apple // num
			ans += apple-(num*a)

print(ans)

'''
a=0
for i in range(int(input())):
    b,c=map(int,input().split())
    a+=c%b
print(a)
'''
