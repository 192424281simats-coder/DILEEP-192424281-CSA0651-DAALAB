nums = [3, 1, 4, 2, 5]

if len(nums) == 0:
    print("List is empty")
else:
    nums.sort()
    print("Sorted List:", nums)
    print("Maximum Element:", nums[-1])
