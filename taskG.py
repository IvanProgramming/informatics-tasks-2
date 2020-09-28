a, b = map(int, input().split())
c, d = map(int, input().split())
res = []
e = 10000
while e != 100000:
    if e % a == b and e % c == d:
        res.append(e)
    e += 1
print(*res)
