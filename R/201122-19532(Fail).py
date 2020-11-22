a, b, c, d, e, f = list(map(int, input().split()))

if d == 0 or e == 0:
	x = (b*f-c*e)/(b*d-a*e)
	y = (c/b)-a*x/b
elif a == 0 or b == 0:
	x = (e*c-f*b)/(e*a-d*b)
	y = (f/e)-d*x/e
print(int(x),int(y))
