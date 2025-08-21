# Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.

def majority_element_in_array(array):
    count =0
    majority = None

    array_length = len(array)
    if array_length == 1:
        return
    else:
        for num in array:
            if count ==0:
                majority = num
            count += (1 if num == majority else -1)                        

    if array.count(majority) > len(array) // 2:
        return majority
    else:
        return -1

array = list(map(int,input("Enter the elements ---> ").split()))
result = majority_element_in_array(array)

if result != -1:
    print("Majority element is ",result)
else:
    print("No Majority Elements ")    