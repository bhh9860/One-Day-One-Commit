#N이 N의 제고ㅂ근보다 크지 않은 어떤 소수로도 나눠지지 않음을 가지고 풂.
n = int(input())
a = list(map(int, input().split()))
count = 0
import math
for j in range(len(a)):
	for i in range(2, int(math.sqrt(a[j]))+1):
		if a[j] % i != 0:
			pass
		else:
			count += 1 #소수가 아니면 1추가
			break;

if 1 in a:
	count += 1 #1도 소수가 아니기에 1추가
print(len(a)-count)
