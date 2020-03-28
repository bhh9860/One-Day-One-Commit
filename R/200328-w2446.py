n = int(input())
star = []
space = 0
for i in range(n, 0, -1):
    a = (' ' * space) + ('*' * (i*2-1))
    space += 1
    star.append(a)
    print(a)

del star[len(star)-1]

for i in range(0, len(star)):
    print(star.pop())
