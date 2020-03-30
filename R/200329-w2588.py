a = int(input())
c = int(input())
b = list(str(c))
b.reverse()
for i in b:
    print(int(i)*a)
print(a*c)
