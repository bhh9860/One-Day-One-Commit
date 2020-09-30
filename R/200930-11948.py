a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = [a, b, c, d]
h = [e, f]
g.sort()
h.sort()
g.pop(0)
h.pop(0)
print(sum(g)+sum(h))
