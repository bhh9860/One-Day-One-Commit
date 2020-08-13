a, b = map(int, input().split())
c = list(map(int, input().split()))

people = a * b
for i in range(5):
	c[i] = c[i] - people
	
print(c[0], c[1], c[2], c[3], c[4])

#a,b=map(int,input().split());[print(int(i)-a*b)for i in input().split()]
