a = int(input())
space = 0
sibal = []
for i in range(a, 0, -1):
	star = 2*i-1
	sibal.append('*' * star)
	sibal.append(space * ' ')
	space+=1

sibal.reverse()

for i in range(len(sibal)):
	print(sibal[i], end='')
	if '*' in sibal[i]:
		print()
		
'''
N = int(input())

for i in range(1,N+1) :
  print(" "*(N-i)+"*"*(i+(i-1)))
'''
