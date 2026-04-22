def min_index_sum(list1, list2):
    index_map = {restaurant: i for i, restaurant in enumerate(list2)}
    min_sum = float('inf')
    result = []
    
    for i, restaurant in enumerate(list1):
        if restaurant in index_map:
            total = i + index_map[restaurant]
            if total < min_sum:
                min_sum = total
                result = [restaurant]
            elif total == min_sum:
                result.append(restaurant)
    
    return result
print("Enter sentence for 2 inputs")
list1 = input("list1: ").strip().split()
list2 = input("list2: ").strip().split()
print(f'list1={list1}')
print(f'list2={list2}')
print(f'Result: {min_index_sum(list1, list2)}')