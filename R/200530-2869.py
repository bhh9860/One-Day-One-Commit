a, b, v = map(int, input().split())
if int(v / (a-b)) != (v / (a-b)):
	d = int(v / (a-b))
else:
	d = (v // (a-b) - 2)
	if d < 0:
		print(1)
	else:
		v -= (a-b) * d
		d += 1
		while (v > 0):
			v -= a
			if v > 0:
				d += 1
				v += b
		print(d)
