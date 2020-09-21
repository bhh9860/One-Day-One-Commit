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
while True:
	ok = True
	im_ans = 0
	sibal = path.copy()
	sibal.insert(len(sibal), sibal.pop(0))
	for i in range(a):
		if b[path[i]][sibal[i]] != 0:
			im_ans += b[path[i]][sibal[i]]
		else:
			ok = False
			break
	if ok == True:
		ans.append(im_ans)
	if not per(path):
		break
		
print(min(ans))
