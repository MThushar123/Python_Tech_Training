
def maximumGap(nums):
    if len(nums) < 2:
        return 0

    nums.sort()

    max_gap = 0

    for i in range(1, len(nums)):
        gap = nums[i] - nums[i - 1]
        max_gap = max(max_gap, gap)

    return max_gap

nums = list(map(int, input("Enter array elements: ").split()))

result = maximumGap(nums)

print("Maximum Gap:", result)