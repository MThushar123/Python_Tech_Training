def max_consecutive_ones(nums):
    max_streak = 0
    current_streak = 0
    
    for num in nums:
        if num == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    
    return max_streak
print("Enter the numbers 0 and 1")
nums = list(map(int, input().strip().split()))
print(f"Input: {nums}")
print(f"Max 1s streak: {max_consecutive_ones(nums)}")