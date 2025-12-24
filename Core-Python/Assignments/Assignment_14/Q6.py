nums = {1, 10, 2, 6, 5}

nums = list(nums)
max_product = 0
pair = ()

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] * nums[j] > max_product:
            max_product = nums[i] * nums[j]
            pair = (nums[i], nums[j])

print(pair, "Product:", max_product)
