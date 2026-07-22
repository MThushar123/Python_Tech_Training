def wiggleSort(nums):
    nums.sort()

    n = len(nums)
    mid = (n + 1) // 2
    left = nums[:mid]
    right = nums[mid:]
    left.reverse()
    right.reverse()

    result = []

    i = j = 0
    while i < len(left) or j < len(right):
        if i < len(left):
            result.append(left[i])
            i += 1
        if j < len(right):
            result.append(right[j])
            j += 1

    return result

nums = list(map(int, input("Enter array elements: ").split()))

result = wiggleSort(nums)

print("Wiggle Sorted Array:", *result)