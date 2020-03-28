#1일 경우를 제외한 2이상의 수부터 제일첫째줄과 두번째줄을 파악해 그대로 출력
#2이상의 수부터 (n, 2n)의 배열. 예)input=2 output = (2, 4) *'' ''* *'' ''*
import copy
num = int(input())
if num != 1:
    a = []
    b = []
    suma = ''
    sumb = ''
    for i in range(1, num+1):
        if i % 2 == 0:
            a.append(' ')
        elif i % 2 != 0:
            a.append('*')

    b = copy.deepcopy(a)
    del b[0]
    if b[len(b)-1] == '*':
        b.append(' ')
    else:
        b.append('*')

    for i in range(num):
        suma += a[i]
        sumb += b[i]

    for i in range(num):
        print(suma)
        print(sumb)

elif num == 1:
    print('*')
