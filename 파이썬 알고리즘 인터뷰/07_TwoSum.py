nums = [2,7,11,15]
target = 9
nums_map = {}

for i, num in enumerate(nums):
    nums_map[num] = i

for i, num in enumerate(nums):
    if target - num in nums_map and i != nums_map[target-num]:
        print(i, nums_map[target-num])
