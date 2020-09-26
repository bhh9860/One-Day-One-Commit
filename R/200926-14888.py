# 다음 순열 구하는 함수
def next(a):
	for i in range(len(a)-1, 0, -1):
		if a[i-1] < a[i]:
			compare = [max(a)+1, 0]
			for j in range(i, len(a)):
				if a[i-1] < a[j]:
					if compare[0] > a[j]:
						compare[0] = a[j]
						compare[1] = j
			b = compare[0]; a[compare[1]] = a[i-1]; a[i-1] = b
			a[i:] = sorted(a[i:])
			return a
'''
입력 예제 )
6
1 2 3 4 5 6
2 1 1 1

ikutsu = 6
num = 1 2 3 4 5 6
operatornum = 2 1 1 1
operatorzeroone = [0, 0, 1, 2, 3](+, +, -, *, //)
'''

ikutsu = int(input())
num = list(map(int, input().split()))
operatornum = list(map(int, input().split()))
operatorzeroone = []
for i in range(4): # operatorzeroone을 만듦
	if i == 0:
		for _ in range(operatornum[i]):
			operatorzeroone.append(0)
	elif i == 1:
		for _ in range(operatornum[i]):
			operatorzeroone.append(1)
	elif i == 2:
		for _ in range(operatornum[i]):
			operatorzeroone.append(2)			
	elif i == 3:
		for _ in range(operatornum[i]):
			operatorzeroone.append(3)
			
operator = ['+', '-', '*', '//']
ans = num[0] # 제일 첫번째 수
for i in range(ikutsu-1):  #operatorzeroone의 숫자대로 num들을 계산함
	if operatorzeroone[i] == 0:
		ans += num[i+1]
	elif operatorzeroone[i] == 1:
		ans -= num[i+1]
	elif operatorzeroone[i] == 2:
		ans *= num[i+1]
	elif operatorzeroone[i] == 3: #-7/6일 때 //로 하면 -1이 나오지 않고 -2가 나옴
		ans /= num[i+1]
		ans = int(ans)

ansmax = ans
ansmin = ans
while next(operatorzeroone):
	ans = num[0]
	for i in range(ikutsu-1):
		if operatorzeroone[i] == 0:
			ans += num[i+1]
		elif operatorzeroone[i] == 1:
			ans -= num[i+1]
		elif operatorzeroone[i] == 2:
			ans *= num[i+1]
		elif operatorzeroone[i] == 3:
			ans /= num[i+1]
			ans = int(ans)
	
	if ans > 1000000000: # 문제 출력 범위 절댓값 10억
		ans = 1000000000
	elif ans < -1000000000:
		ans = -1000000000
		
	if ansmax < ans:
		ansmax = ans
	elif ansmin > ans:
		ansmin = ans
		
print(ansmax)
print(ansmin)
