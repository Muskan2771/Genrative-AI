nums = [1, 2, 3, 4, 5]
target = 6

result = set()

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == target:
                result.add((nums[i], nums[j], nums[k]))

print(result)