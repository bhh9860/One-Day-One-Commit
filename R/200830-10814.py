a = int(input())
b = []
count = 0
for i in range(a):
	b.append(list(input().split()))
	b[i][1:1] = [count]
	count += 1

for j in range(len(b)): #14 < 123이지만 sort하면 순서는 123, 14가 되므로 앞에 0을 붙여 014 123 으로 되도록 만듦.
	if len(b[j][0]) != 3:
		b[j][0] = '0'*(3-len(b[j][0])) + b[j][0]
b.sort()
[print(str(int(b[i][0])) + ' ' + b[i][2]) for i in range(len(b))]
