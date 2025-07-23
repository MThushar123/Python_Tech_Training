#from an array of integers for each elements, find the next greater elements to it right. 
# return an array of answers . if no greater elements exists use -1

def greater_element_in_array(array):
    array_length = len(array)

    result = [-1] * array_length
    stack = []

    if array_length <=1:
        print("Array length is less than 1. So there are greater elements")
        exit
    else:
        for i in range(array_length):
            while stack and array[i] > array[stack[-1]]:
                index = stack.pop()
                result[index] = array[i]
            stack.append(i)
    return result

array = [3,6,5,9,1,4,8,6,4]   
print(greater_element_in_array(array))
