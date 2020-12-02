jo, dan, team = list(map(int, input().split()))
m = jo // 2
na = jo % 2
n = jo - na

if dan < m:
    a = m-dan
    n -= a*2
    m -= a
    na += 3*a

if na - team < 0:
    b = 0
    while True:
        b += 1
        if 3*b >= 2:
            break
    n -= b*2
    m -= b
    na += 3*b
    na -= team

print(m)
