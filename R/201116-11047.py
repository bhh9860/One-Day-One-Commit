a, b = list(map(int, input().split()))
coin = []
for i in range(a):
	coin.append(int(input()))

count = 0
coin.reverse()

while True:
	if b == 0:
		break
	for i in coin:
		if b >= i:
			count += b//i
			b %= i

print(count)
