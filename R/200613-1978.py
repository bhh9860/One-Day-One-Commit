#매우 무식하게 함.
#소수 구하는 알고리즘 검색해서 다시 만들어볼 생각.
a = []
b = []
count = 0
for i in range(2, 1001): #1을 제외한 2부터 1000까지 리스트 만들기
	a.append(i)
	
for i in range(2, 1001): #2부터 1000까지 나눠보기
	for j in range(len(a)): #len(a)만큼 i로 나누기
		if a[j] == i: #나눠서 0나오면 b에 집어넣음
			continue
		if a[j] % i == 0:
			b.append(a[j])

		else:
			pass
	for k in range(len(b)): #모두 소수가 아닌것들이기에 a에서 제외시킴
		del a[a.index(b[k])]
	b = []

n = int(input())
number = input().split()
for s in range(len(number)):
	if a.count(int(number[s])) == 1: #a에 있는 숫자는 소수.
		count += 1
	else:
		continue
		
print(count)
