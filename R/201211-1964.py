n = int(input())
dot = 1
a = 0
for i in range(n):
	a = 4+3*i
	dot += a
	
print(dot%45678)
