n = int(input())
c = 0
nums = []
while c >= n:
    if c % 2 == 0:
        nums.append(c)
    c += 1
print(*nums)
