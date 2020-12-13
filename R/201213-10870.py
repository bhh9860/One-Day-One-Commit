a = [0, 1]
n = int(input())

def fibo(n, i):
	b = a[i] + a[i+1]
	a.append(b)
	i += 1
	if i >= n:
		return a
	fibo(n, i)
	
fibo(n, 0)
print(a[n])
