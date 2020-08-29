box, count = map(int, input().split())
box = [0] * box

for _ in range(count):
	a, b, c = map(int, input().split())
	for i in range(a-1, b):
		box[i] = c
[print(i, end=' ') for i in box]
