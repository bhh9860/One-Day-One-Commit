#문제 입출력 효율성을 위해
import sys
input=sys.stdin.readline

num, find = list(map(int, input().split()))
juso = {}
for _ in range(num):
    a, b = input().split()
    juso[a] = b

for _ in range(find):
    print(juso[input().strip()])
