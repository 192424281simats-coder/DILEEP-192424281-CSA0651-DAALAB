nums = [1, 2, 1]

total = 0

for i in range(len(nums)):
    s = set()
    for j in range(i, len(nums)):
        s.add(nums[j])
        total += len(s) ** 2

print("Sum =", total)
