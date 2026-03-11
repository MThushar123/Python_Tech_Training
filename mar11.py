
def merge_two_lists(list1, list2):

    result = []

    i = 0  
    j = 0  
    
    # Compare until one list ends
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1  
        else:
            result.append(list2[j])
            j += 1  
    
    # Add remaining from list1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    
    # Add remaining from list2
    while j < len(list2):
        result.append(list2[j])
        j += 1
    
    return result

print(" MERGE TWO LISTS")
print("List 1 numbers separated by space:")
list1 = list(map(int, input().split()))

print("List 2 numbers separated by space:")
list2 = list(map(int, input().split()))

print(f"\n Input:")
print(f"List 1: {list1}")
print(f"List 2: {list2}")

merged = merge_two_lists(list1, list2)
print(f"\n Merged: {merged}")

