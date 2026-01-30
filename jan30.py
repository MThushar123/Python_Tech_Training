def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

print("Enter numbers separated by spaces:")
user_input = input().strip()
if user_input:
    num_list = [int(x) for x in user_input.split()]
    result = find_max(num_list)
    print(f"Maximum number: {result}")
else:
    print("No input.")
