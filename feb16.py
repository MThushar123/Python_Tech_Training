def has_duplicates(numbers):
    seen = []  # List to track numbers we've seen
    
    for num in numbers:
        if num in seen:
            return True  # Found duplicate!
        seen.append(num)
    
    return False  # No duplicates found

# Interactive usage
print("Enter numbers separated by spaces:")
user_input = input().strip()
if user_input:
    num_list = [int(x) for x in user_input.split()]
    
    if has_duplicates(num_list):
        print(" YES - List contains DUPLICATES!")
    else:
        print(" NO - All numbers are UNIQUE!")
else:
    print("No input!")
