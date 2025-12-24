nums = [1, 2, 3, 4, 5]
target = 5

pairs = set()

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.add((nums[i], nums[j]))

print(pairs)
