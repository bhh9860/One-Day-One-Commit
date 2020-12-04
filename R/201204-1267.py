count = int(input())
call = list(map(int, input().split()))
young = 0
min = 0

for i in call:
	young += (i//30)+1
young *= 10

for i in call:
	min += (i//60)+1
min *= 15

if young == min:
	print('Y', 'M', min)
elif young > min:
	print('M',min)
elif young < min:
	print('Y',young)
