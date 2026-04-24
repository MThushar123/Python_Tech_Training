def triangle_number(nums):
    nums.sort()
    n = len(nums)
    count = 0
    
    for k in range(n-1, 1, -1):
        left, right = 0, k - 1
        while left < right:
            if nums[left] + nums[right] > nums[k]:
                count += right - left
                right -= 1
            else:
                left += 1
    
    return count
print("Enter the number")
nums = list(map(int, input().strip().split()))
print(f'Input: {nums}')
print(f'Triangles: {triangle_number(nums)}')