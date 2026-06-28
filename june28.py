def maxRotateFunction(nums):
    n = len(nums)

    if n == 0:
        return 0

    total_sum = sum(nums)

    current = 0
    for i in range(n):
        current += i * nums[i]

    maximum = current

    for k in range(1, n):
        current = current + total_sum - n * nums[n - k]
        maximum = max(maximum, current)

    return maximum

nums = list(map(int, input("Enter array elements: ").split()))

result = maxRotateFunction(nums)

print("Maximum Rotation Function Value:", result)