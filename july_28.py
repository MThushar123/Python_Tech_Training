def merge_sort(arr):
    if len(arr) <= 1:
        return arr  

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # Recursive sort frm the left half side
    right = merge_sort(arr[mid:])   # Recursive sort frm the right half side

    result = []
    i = j = 0

    # Merging two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # insertinfg remaining elements from either half
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("Sorted:", merge_sort([5, 2, 9, 1, 7]))