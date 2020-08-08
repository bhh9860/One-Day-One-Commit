import math
n = int(input())
r = int(input())-n

n = n+r-1

print(math.factorial(n) // (math.factorial(n-r) * math.factorial(r)))
