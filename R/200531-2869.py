#풀이
"""
a = 올라가는 높이 b = 내려가는 높이 v = 나무높이(올라간 뒤 남은 나무 높이) d = day 올라간 날
1.  v/(a-b)로 계산하면 마지막 날에 하강까지 계산되기 때문에 계산이 틀려짐. 때문에
2. 마지막 전날까지 올라간 높이를 계산해야함. 먼저 마지막 전날을 계산함. 식은 d = (v-a) // (a-b). 소수점 무시를 위해 //를 사용.
3. 마지막 전날까지 올라간 높이는 nv = d*(a-b). #nv = nise v
4. 올라왔으니 남은 나무의 높이는 v -= nv
5. 다시 올라갈껀데 v가 만약 a보다 크다면 올라가도 한번은 하강하게 돼있음. 예를 들어 v가 5, a가 4이면 올라갔다 한번은 내려가고 그 다음날에 정상에 도달하기 때문에 d += 2
6. 만약 v가 a보다 작거나 같다면 그 날 바로 정상에 도달하기 때문에 d += 1
"""
a, b, v = map(int, input().split())
d = (v-a) // (a-b)
v = v - ((a-b) * d)
if v > a:
	d += 2
else:
	d += 1
print(d)
