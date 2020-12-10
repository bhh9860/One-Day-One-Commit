import sys
input=sys.stdin.readline

num = int(input())
ans = []
for _ in range(num):
	a = input().split()
	if a[0] == 'push':
		ans.append(a[1])
	elif a[0] == 'pop':
		print(ans.pop(0) if len(ans)>0 else -1)
	elif a[0] == 'size':
		print(len(ans))
	elif a[0] == 'empty':
		print(1 if len(ans)==0 else 0)
	elif a[0] == 'front':
		print(ans[0] if len(ans)>0 else -1)
	elif a[0] == 'back':
		print(ans[-1] if len(ans)>0 else -1)

