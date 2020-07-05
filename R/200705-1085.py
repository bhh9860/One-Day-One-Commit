x, y, w, h = map(int, input().split())
a = [abs(0-x), abs(0-y), w-x, h-y]
print(min(a))
