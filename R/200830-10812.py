'''
문제 해결 방법
예시)
input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 2, b = 8, c = 4
output = [1, 4, 5, 6, 7, 2, 3, 8, 9, 10]

2번째 박스부터 8번째 박스까지 통째로 rinzy에 이식, input의 해당 박스들은 삭제
a부터 c의 앞 상자가 뒤로 가기만 하면 됨
rinzy_a를 a:c(2, 3)으로 잡고, rinzy의 해당 박스는 삭제한 뒤, 제일 끝에 삽입.
[2, 3, 4, 5, 6, 7] -> [4, 5, 6, 7, 2, 3]
그대로 input의 해당 리스트에 삽입
'''
a, count = map(int,input().split())
box = []
[box.append(i) for i in range(1, a+1)]
for _ in range(count):
	a, b, c = map(int, input().split())
	rinzy = box[a-1:b]; del box[a-1:b]
	rinzy_a = rinzy[:c-a]; del rinzy[:c-a]
	[rinzy.append(i) for i in rinzy_a]
	aaa = 0
	for i in range(a-1, b):
		box.insert(i, rinzy[aaa])
		aaa += 1
[print(i, end=' ') for i in box]
