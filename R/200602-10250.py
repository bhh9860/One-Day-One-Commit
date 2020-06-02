for i in range(int(input())):
	a, b, v = map(int, input().split())
	A = v / a
	if A != int(A):
		A = int(A)
		A += 1
	if type(A) == float():
		A = int(A)
	A = str(int(A))
	B = v % a
	if B == 0:
		B = a
	B = str(B)
	if int(A) < 10:
		A = '0' + A
	print(B+A)
