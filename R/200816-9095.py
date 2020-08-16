for i in range(int(input())):
	a = int(input())
	ans = 0
	for i0 in range(1, 4):
		if a == i0:
			ans += 1
		for i1 in range(1, 4):
			if a == i0+i1:
				ans += 1
			for i2 in range(1, 4):
				if a == i0+i1+i2:
					ans += 1
				for i3 in range(1, 4):
					if a == i0+i1+i2+i3:
						ans += 1
					for i4 in range(1, 4):
						if a == i0+i1+i2+i3+i4:
							ans += 1
						for i5 in range(1, 4):
							if a == i0+i1+i2+i3+i4+i5:
								ans += 1
							for i6 in range(1, 4):
								if a == i0+i1+i2+i3+i4+i5+i6:
									ans += 1
								for i7 in range(1, 4):
									if a == i0+i1+i2+i3+i4+i5+i6+i7:
										ans += 1
									for i8 in range(1, 4):
										if a == i0+i1+i2+i3+i4+i5+i6+i7+i8:
											ans += 1
										for i9 in range(1, 4):
											if a == i0+i1+i2+i3+i4+i5+i6+i7+i8+i9:
												ans += 1
												
	print(ans)
	
'''
n = int(input())

dp = [0 for i in range(11)]

dp[0:4]=[0,1,2,4]

for j in range(n):
    num = int(input())
    for i in range(4,num+1):
        dp[i] = dp[i-1]+ dp[i-2] + dp[i-3]
    print(dp[num])
'''
