n = int(input())
star = []
for i in range(n, 0, -1):
    a = '*' * (i*2-1)
    star.append(a)
    print(a)

del star[len(star)-1]

for i in range(0, len(star)):
    print(star.pop())

***
 *
