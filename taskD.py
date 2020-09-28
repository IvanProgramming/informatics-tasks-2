a, b = map(int, input().split())
while a != (b + 1):
    print(f"{a}*{a}={a * a}")
    a += 1
