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
anslist = []
for j in ans:
	anslist.append(hito[])
