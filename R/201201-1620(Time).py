import sys
input=sys.stdin.readline

a = {}
n, m = list(map(int, input().split()))
for i in range(n):
    a[input().strip()] = str(i+1)

for i in range(m):
    b = str(input()).strip()
    try:
        int(b)
        print([v for v, k in a.items() if k == b][0])
    except ValueError:
        print(a.get(b))
