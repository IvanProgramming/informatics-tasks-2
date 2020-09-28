n = int(input())
c = 1
nums = []
while len(nums) != n:
    if c % 2 == 0:
        nums.append(c)
    c += 1
print(*nums)
