def unique_elements(lst):
    seen = set()
    uniques = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            uniques.append(item)
    count = len(uniques)
    return uniques, count

print("Enter numbers separated by spaces:")
user_input = input().strip()
if user_input:
    num_list = [int(x) for x in user_input.split()]
    uniques, count = unique_elements(num_list)
    print(f"Unique elements: {uniques}")
    print(f"Count of unique elements: {count}")
else:
    print("No input is given.")
