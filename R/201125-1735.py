#1
a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

#2
if b < d:
	g = b
	b = d
	d = g
	g = a
	a = c
	c = g

#3
x1, x2 = b, d	
# 최대공약수 = x1
while x2 != 0:
	n = x1 % x2
	x1 = x2
	x2 = n

#4
# 최소공배수 = x3
x3 = b*d // x1

#5
a *= x3 // b
c *= x3 // d
#6
b, d = x3, x3
e = a+c
f = b

#7
# e/f를 기약분수로
x4, x5 = max(e, f), min(e, f)
while x5 != 0:
	n = x4 % x5
	x4 = x5
	x5 = n

e //= x4
f //= x4
print(e, f)
