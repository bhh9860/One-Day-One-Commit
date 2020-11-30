a = int(input())
acard = list(map(int, input().split()))
b = int(input())
bcard = list(map(int, input().split()))

adict = {}
for i in acard:
    if not adict.get(i):
        adict[i] = 1
    else:
        adict[i] += 1

'''안됨'''
'''[print(adict.get(i), end = ' ') if not adict.get(i) == None else '0' for i in bcard]'''


ans = []
for i in bcard:
    anscard = adict.get(i)
    if not anscard == None:
        ans.append(anscard)
    else:
        ans.append(0)
        
[print(i, end = ' ') for i in ans]
