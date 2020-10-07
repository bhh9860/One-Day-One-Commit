c, a, b = list(map(int, input().split()))
x, y = a, b
i = int(((x**2*c**2)/(x**2+y**2))**0.5)
j = int((c**2-i**2)**0.5)
print(i, j)
