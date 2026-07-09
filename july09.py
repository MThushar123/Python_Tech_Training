def isMonotonic(nums):
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        elif nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing

nums = list(map(int, input("Enter array elements: ").split()))

result = isMonotonic(nums)

print("Is Monotonic Array:", result)