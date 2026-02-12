def sum_nested_list(nested):
    total = 0
    for item in nested:
        if isinstance(item, list):
            # If it's a list, recurse to sum inside
            total += sum_nested_list(item)
        else:
            # If it's a number, add it
            total += item
    return total

print("Enter nested list (e.g. [1,2,[3,4],5] or [[1,2],[3,[4,5]]]):")
user_input = input().strip()
import ast
try:
    nested_list = ast.literal_eval(user_input)
    result = sum_nested_list(nested_list)
    print(f"Total sum: {result}")
except:
    print("Invalid list format.......!")
