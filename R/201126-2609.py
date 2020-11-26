a, b = list(map(int, input().split()))
if a < b:
	a, b = b, a
c, d = a, b
while b != 0:
	n = a % b
	a = b
	b = n

print(a)
print(c*d // a)

'''
숏코딩 레게노
a,b=map(int,input().split());L=a*b
while b:a,b=b,a%b
print(a,L//a)
'''
