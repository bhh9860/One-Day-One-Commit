a = str(input())
b = str(input())
ahour = int(a[0:2])
amin = int(a[3:5])
asec = int(a[6:8])
bhour = int(b[0:2])
bmin = int(b[3:5])
bsec = int(b[6:8])



if asec > bsec:
    bmin -= 1
    bsec -= asec
    bsec += 60

if amin > bmin:
    bhour -= 1
    bmin -= amin
    bmin += 60

bhour -= ahour

if len(str(bhour)) == 1:
    bhour = list(bhour)
    bhour.insert(0, 1)
if len(str(bmin)) == 1:
    bmin = list(bmin)
    bmin.insert(0, 1)
if len(str(bsec)) == 1:
    bsec = list(bsec)
    bsec.insert(0, 1)

bhour = list(map(str, bhour))
bmin = list(map(str, bmin))
bsec = list(map(str, bsec))

print(bhour[0]+bhour[1]+':'+bmin[0]+bmin[1]+':'+bsec[0]+bsec[1])
