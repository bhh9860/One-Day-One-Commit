n, m, k = list(map(int, input().split()))
na = 0
if n % 2 != 0:
    n -= 1
    na += 1


if n > m*2:
    a = n-(m*2)
    n -= a
    na += a
elif n < m*2:
    a = m-(n//2)
    m -= a
    na += a

if na - k < 0:
    b = k - na
    c = b // 3
    if b % 3 > 0:
        c += 1
    n -= c*2
    m -= c
    na += c*3

print(m)
