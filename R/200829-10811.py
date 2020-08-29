a, count = map(int, input().split())
box = []; [box.append(i) for i in range(1, a+1)]
for _ in range(count):
	a, b = map(int, input().split())
	box[a-1:b] = list(reversed(box[a-1:b]))

[print(i, end=' ') for i in box]
