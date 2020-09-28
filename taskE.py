a, b = map(int, input().split())
res = 0
while a != (b + 1):
    res += a ** 2
    a += 1
print(res)
