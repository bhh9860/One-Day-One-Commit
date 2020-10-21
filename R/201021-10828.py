import sys
input=sys.stdin.readline

def push(a, x):
	a.append(x)
	return

def pop(a):
	if len(a) == 0:
		print('-1')
		return 
	else:
		print(a.pop())
		return
		
def size(a):
	print(len(a))
	return

def empty(a):
	if len(a) == 0:
		print('1')
		return
	else:
		print('0')
		return

def top(a):
	if len(a) == 0:
		print('-1')
		return
	else:
		print(a[len(a)-1])
		return
		
stack = []		
for _ in range(int(input())):
	a = input().split()
	if len(a) == 2:
		push(stack, int(a[1]))
	else:
		if a[0] == 'pop':
			pop(stack)
		elif a[0] == 'size':
			size(stack)
		elif a[0] == 'empty':
			empty(stack)
		elif a[0] == 'top':
			top(stack)
