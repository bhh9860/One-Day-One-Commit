a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if b % d == 0:
	b //= d
else:
	b //= d
	b += 1

if c % e == 0:
	c //= e
else:
	c //= e
	c += 1
	
f = [b, c]
print(a-max(f))
