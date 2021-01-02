for i in range(int(input())):
    a, b = list(map(int, input().split()))
    if a > 0 and b > 0:
        ans = int((a+b)*b/2)
    elif a < 0 and b > 0:
        a = abs(a)
        ans = int((1+b)*b/2)
        ans -= int((1+a)*a/2)
    elif a < 0 and b < 0:
        ans = 0
        for j in range(a, b+1, 1):
            ans += j
    print(f'Scenario #{i+1}:')
    print(ans)
