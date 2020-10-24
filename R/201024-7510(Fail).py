for i in range(int(input())):
    print('Scenario #{0}'.format(i+1))
    a = list(map(int, input().split()))
    a.sort()
    if a[2]**2 == a[1]**2 + a[0]**2:
        print('yes')
        print()
    else:
        print('no')
        print()
