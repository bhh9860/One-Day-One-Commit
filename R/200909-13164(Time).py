hitos, gumi = list(map(int, input().split())) #人たち、組
hito = [] #人
hito = list(map(int, input().split()))
tigai = [] #違い
[tigai.append(hito[i+1]-hito[i]) for i in range(hitos-1)]
ans = []

for i in range(gumi-1):
	a = max(tigai)
	if tigai.count(a) == 1:
		ans.append(tigai.index(a))
		tigai[tigai.index(a)] = 0
	else:
		ans.append(tigai.index(a))
		tigai[tigai.index(a)] = 0
	
ans.sort()	

k = 0
for i in ans:
	hito.insert(i+1+k, -1)
	k += 1 #추가하면 추가할 수록 뒤로 밀리기 때문에 k로 방지
	
k = []
anslist =[]
for i in hito:
	if i != -1:
		k.append(i)
	else:
		anslist.append(k)
		k = []
anslist.append(k)

saigo = 0
for i in anslist:
	if len(i) == 1:
		pass
	else:
		saigo += max(i) - min(i)

print(saigo)
