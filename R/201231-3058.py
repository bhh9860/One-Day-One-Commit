for i in range(int(input())):
  a = list(map(int, input().split()))
  jjak = []
  for j in a:
    if j % 2 == 0:
      jjak.append(j)
  print(sum(jjak), min(jjak))