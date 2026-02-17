def has_subset_sum(nums, target):
    """Check if any subset sums to target (brute force - tries all combinations)"""
    n = len(nums)
    
    # Try all possible subsets (2^n combinations)
    for i in range(1 << n):  # 1<<n = 2^n
        subset_sum = 0
        subset = []
        
        # Check which elements are in this subset
        for j in range(n):
            if i & (1 << j):  # Bit j is set
                subset_sum += nums[j]
                subset.append(nums[j])
        
        if subset_sum == target:
            print(f" YES! Found subset: {subset}")
            return True
    
    print(" NO subset sums to target")
    return False

print("Enter numbers (space separated):")
nums = [int(x) for x in input().split()]
print("Enter target sum:")
target = int(input())

has_subset_sum(nums, target)
