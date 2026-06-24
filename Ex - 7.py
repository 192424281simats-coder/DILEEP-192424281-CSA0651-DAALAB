nums = [3, 7, 3, 5, 2, 5, 9, 2]

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("Unique Elements:", unique)
