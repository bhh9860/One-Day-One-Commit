a, count = map(int, input().split())
box = []
[box.append(i+1) for i in range(a)]
for _ in range(count):
	swap1, swap2 = map(int, input().split())
	swap1 -= 1; swap2 -= 1
	b = box[swap1]; box[swap1] = box[swap2]; box[swap2] = b

[print(i, end=' ') for i in box]
