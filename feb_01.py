def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# User input example
print("Enter a nested list (e.g., [[1,2],[3,[4,5]],6]):")
user_input = input().strip()
import ast
try:
    nested_list = ast.literal_eval(user_input)
    result = flatten_list(nested_list)
    print(f"Flattened list: {result}")
except:
    print("Invalid input")
