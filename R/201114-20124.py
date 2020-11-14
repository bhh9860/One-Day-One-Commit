a = []
b = int(input())
for _ in range(b):
	a.append(list(input().split()))

compare = 0
people = []
for i in range(b):
	if compare < int(a[i][1]):
		compare = int(a[i][1])
		people = []
		people.append(a[i][0])
	elif compare == int(a[i][1]):
		people.append(a[i][0])

people.sort()
print(people[0])
