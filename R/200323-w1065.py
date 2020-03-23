han = [] #한수면 append로 추가
num = int(input()) #값 받아요
if num <= 99 and num >= 1:#1~99는 무조건 한수. 고로 num이 1~99사이에 있다면, 1~num까지 한수.
    for i in range(num):
        han.append(i+1)
elif num > 99: #1~99의 한수포함은 확정. 그 이후 한수 걸러내기.
    for i in range(1, 100): #1~99
        han.append(i) 
    for a in range(100, num+1):#100부터 num까지 한수 걸러내기.
        b = list(map(int,list(str(a)))) #a를 리스트로 바꾸되, 리스트값들은 int형으로
        for i in range(len(b)-2): #예를 들어 세자릿수일때, 1번만 검사하면 됨. 3->1번 4->2번... 이므로 -2
            one = b[i] - b[i+1] #세자릿수 -> 1번 인 이유 두자리수씩 두번 검사. 예)123 -> (1,2), (2,3) = 1번
            two = b[i+1] - b[i+2]
            if one == two: #모든 자릿수의 차이가 같아야 하므로 if걸고
                if i+3 == len(b): #끝자리수까지 모두 차이가 같으면 append
                    han.append(a)
                else:
                    pass
            else: #한번이라도 차이가 틀리면 그 값은 한수가 아님.
                break
print(len(han))
