'''원 구하는 공식은 파이알제곱이니까 	rrpi맞고
택시기하학은 아직도 잘 모르긴 하겠는데 정사각형의 대각선의 절반이 r이니까
한 변을 먼저 구하자면
한 변 = 루트(2 * r**2)인데 넓이 구하는거니까 한 변의 제곱이므로 루트소거.
즉 2 * r * r임.'''

import math
r = int(input())
circle = r * r * math.pi
taxi = 2 * r * r
print(round(circle, 6))
print('%.6f' %taxi)
