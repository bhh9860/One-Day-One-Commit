a = []
for i in range(10):
    a.append(int(input())) #값 a에 10개 받기

b = []    
for i in range(10):
    b.append(a[i] % 42) #받은 값 모두 42로 나눠 나머지 b에 넣기

b = list(set(b)) #중복제거

print(len(b))
