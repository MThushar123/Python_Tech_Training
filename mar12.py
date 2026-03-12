def remove_duplicates_easy(nums):

    if not nums:
        return [], 0

    nums.sort()
    
    next_pos = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[next_pos] = nums[i]
            next_pos += 1
    
    unique_nums = nums[:next_pos]
    return unique_nums, next_pos

print("Enter any numbers sorted or unsorted:")

numbers = list(map(int, input().split()))
print(f"Original: {numbers}")

unique_list, length = remove_duplicates_easy(numbers)

print(f"Unique:  {unique_list}")