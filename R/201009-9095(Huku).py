def go(n):
	if n == 0:
		return 1
	if n < 0:
		return 0
	count = 0
	
	for i in range(1, 4):
		count += go(n-i)
	return count

for i in range(int(input())):
	n = int(input())
	print(go(n))


'''def go(n, count):
	if n == count:
		return 1
	if n < count:
		return 0
	
	ans = 0
	
	for i in range(1, 4):
		ans += go(n, count+i)
	
	return ans

n = int(input())
print(go(n, 0))'''
