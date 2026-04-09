def third_max(nums):
    first = second = third = float('-inf')
    
    for num in nums:
        if num == first or num == second or num == third:
            continue
        if num > first:
            third, second, first = second, first, num
        elif num > second:
            third, second = second, num
        elif num > third:
            third = num
    
    return third if third != float('-inf') else first
print("Enter the numbers")
nums = list(map(int, input().strip().split()))
print(f"Input: {nums}")
print(f"Third max: {third_max(nums)}")