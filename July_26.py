#binary search

def binary_search(array,target):
    array = sorted(array)
    array_length = len(array)
    left =0
    right = array_length -1

    while left <=right:
        mid_value = (left + right)//2

        if target == array[mid_value]:
            print("Target Value is found ",mid_value)
            return
        elif array[mid_value] < target:
            left = mid_value +1
        else:
            right = mid_value -1
    print("VAlue NOT FOUND In Array")
    return -1

array = [8,6,3,2,4,8,9,6,1,5]
target = 10

binary_search(array,target)