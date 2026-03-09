def remove_duplicates(numbers):

    if not numbers:
        return 0
    
    write_pos = 1
    
    for read_pos in range(1, len(numbers)):
        
        if numbers[read_pos] != numbers[read_pos - 1]:
            numbers[write_pos] = numbers[read_pos]
            write_pos += 1
    
    return write_pos

def safe_remove_duplicates():
    print("=== Remove Duplicates SORTED Array Only ===")
    print("Enter numbers:")
    user_input = input().strip()
    
    if user_input:
        nums = [int(x) for x in user_input.split()]
        print(f"Input:     {nums}")
        
        nums.sort()
        print(f"Sorted:    {nums}")
        
        new_size = remove_duplicates(nums)
        
        print(f"Unique:    {nums[:new_size]}")
        print(f"Length:    {new_size}")
        print(f"Ignored:   {nums[new_size:]}")
    else:
        print("No input!")

# Test it
safe_remove_duplicates()
