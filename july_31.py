#slidinf window for second largest number
def second_largest_in_sliding_window(nums, k):
    if len(nums) < 2 or k < 2:
        return []

    result = []

    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        
        first, second = float('-inf'), float('-inf')
        for num in window:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num
        
        if second == float('-inf'):
            result.append(None) 
        else:
            result.append(second)

    return result

nums = [1, 3, 2, 5,4]
k = 3
print(second_largest_in_sliding_window(nums, k))