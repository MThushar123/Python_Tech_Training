def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left  

nums = list(map(int, input("Enter array elements: ").split()))

result = findPeakElement(nums)

print("Peak Element Index:", result)
print("Peak Element:", nums[result])