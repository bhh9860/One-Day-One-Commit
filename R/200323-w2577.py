a = int(input()) #a받고
b = int(input()) #b받고
c = int(input()) #c받고
d = sorted(list(str(a*b*c))) #abc 곱해서 리스트로 하나씩 쪼개서 솔트해주고
e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #0부터 9까지 1씩 더해줄 배열 만들고
for i in range(len(d)):
    e[int(d[i])] += 1 #0~9 판단해서 배열e의 각 자릿수에 1 더하기
for i in range(10):
    print(e[i])
