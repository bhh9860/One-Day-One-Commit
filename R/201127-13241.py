a, b = map(int, input().split())
if a < b:
    a, b = b, a

c, d = a, b

while d != 0:
    n = c % d
    c = d
    d = n

print(a*b//c)
