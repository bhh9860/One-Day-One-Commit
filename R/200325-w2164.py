#200324의 2164는 맞긴 하지만 시간초과.
#이하풀이법은 출력결과의 규칙을 찾아 구현.
#1부터 넣었을 때, [1] [2] [2,4] [2,4,6,8] [2,4,6,8,10,12,14,16]...
#2의 n승으로 끝남.
#규칙은 출력받은 (num)보다 작은 최대의 2의n승을 back으로 정의.
#(num-back)*2.

two = []
num = int(input())
a = 2
while (a<500000):
    two.append(a)
    a *= 2

for i in range(len(two)):
    if two[i] == num:
        print(num)
        break
    elif num == 1:
        print(num)
        break
    elif two[i] < num:
        pass
    elif two[i] > num:
        back = two[i-1]
        print((num-back)*2)
        break

if num > 262144:
    print((num-262144)*2)
