n, k, q = list(map(int, input().split()))
nr = []
sender = []
nrcount = []
for i in range(k):
    a = input().split()
    nr.append(int(a[0]))
    sender.append(a[1])
    if nr[i] > nr[i-1]:
        nrcount.append(i)
nrcount.insert(0, nrcount[0]-1)

a = [nr[q-1], sender[q-1]]

if nr[-1] == nr[nrcount[a[0]-1]]:
    anssender = sender[nrcount[a[0]-1]:]
else:
    anssender = sender[nrcount[a[0]-1]:a[0]]

anssender = sorted(list(set(anssender)))

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
people = []
for i in range(n):
    people.append(alpha[i])

for j in anssender:
    if j in people:
        del people[people.index(j)]

if len(people) == 0:
    print('-1')
else:
    print(' '.join(people))
