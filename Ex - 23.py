id="1ekx89"
nums = [1,2,3,1]

for i in range(len(nums)):
    left = nums[i-1] if i > 0 else -1
    right = nums[i+1] if i < len(nums)-1 else -1

    if nums[i] > left and nums[i] > right:
        print(i)
        break
