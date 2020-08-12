# 29 = E_x, S_y, M_z
# E_x == 15 * x + E
# S_y == 28 * y + S
# M_z == 19 * z + M
# E는 고정, x를 1씩 증가시키고 E_x == S_y == M_z의 상황을 만들기 위해 y와 z도 1씩 증가시키는 알고리즘
E, S, M = map(int, input().split())
if E == S == M:
	print(E)
else:
	x = 1; y = 0; z = 0 # E, S, M이 모두 같지 않다는 것은 최소한 E는 15를 넘음.
	# 4 19 19 같은 오직 x는 1 이외는 0의 상황을 위해 선언
	E_x = 15 * x + E
	S_y = 28 * y + S
	M_z = 19 * z + M
	while (E_x != S_y or S_y != M_z): # !(a==b==c) == (a!=b or b!=c)
		E_x = 15 * x + E # 와일문 끝에 x+=1을 위해 선언
		while E_x-28 >= S_y:
			y += 1
			S_y = 28 * y + S
		while E_x-19 >= M_z:
			z += 1
			M_z = 19 * z + M
		x += 1
	print(E_x)
