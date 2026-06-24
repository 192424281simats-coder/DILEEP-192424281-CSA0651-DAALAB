nums1 = [2, 3, 2]
nums2 = [1, 2]

answer1 = 0
answer2 = 0

for num in nums1:
    if num in nums2:
        answer1 += 1

for num in nums2:
    if num in nums1:
        answer2 += 1

print([answer1, answer2])
