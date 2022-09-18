idx, n, k = 0, int(input()), int(input()) - 1
nums = list(range(1, n + 1))
while len(nums) > 1:
    idx = (idx + k) % len(nums)
    nums.pop(idx)
print(nums[0])