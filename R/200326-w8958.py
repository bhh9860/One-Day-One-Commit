for i in range(int(input())): #테스트 케이스의 개수
    case = list(input()) #테스트 케이스 입력
    count = 0 #연속되는 O카운트
    num = 0 #카운트들의 총 합
    for i in range(len(case)):
        if case[i] == 'O': #O면 카운트+1 뒤 카운트를 넘에 더해줌
           count += 1
           num += count 
        else:
            count = 0 #X면 카운트 초기화. 초기화되면 넘에 더해줄 필요 없음
    print(num)
