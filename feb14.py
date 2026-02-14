def find_intersection(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

print("Enter first list with numbers separated by space:")
list1 = [int(x) for x in input().split()]
print("Enter second list with numbers separated by space:")
list2 = [int(x) for x in input().split()]

intersection = find_intersection(list1, list2)
print(f"Intersection: {intersection}")
