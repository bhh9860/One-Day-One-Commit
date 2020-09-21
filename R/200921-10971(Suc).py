#다음순열 구하는 함수
def per(b):
	for i in range(len(b)-1, 0, -1):
		if b[i] > b[i-1]:
			c = []
			for j in b[i:]:
				if b[i-1] < j:
					c.append(j)
			c.sort()
			d = c[0]; b[b.index(c[0])] = b[i-1]; b[i-1] = d
			b[i:] = sorted(b[i:])
			return b

a = int(input())
path = [i for i in range(a)]
b = [list(map(int, input().split())) for _ in range(a)]
ans = []

while True: #per(path)가 더이상 나오지 않을 때까지
	ok = True
	im_ans = 0 #임시 ans
	sibal = path.copy()
	sibal.insert(len(sibal), sibal.pop(0)) #문제의 키 포인트. 정답이 0, 1, 2, 3(->0) 이라면 0[1], 1[2], 2[3], 3[0]을, 즉 1, 2, 3, 0을 더해야 맞기 때문에 제일 앞 숫자를 제일 뒤로 옮겨줌. 이것때문에 이틀을 태움;
	for i in range(a):
		if b[path[i]][sibal[i]] != 0:
			im_ans += b[path[i]][sibal[i]]
		else: #0이라면
			ok = False
			break
	if ok == True: #0이 껴 있지 않다면
		ans.append(im_ans)
	if not per(path):
		break
		
print(min(ans))
