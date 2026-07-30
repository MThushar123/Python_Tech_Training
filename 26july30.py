def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2

        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]

arr = list(map(int, input("Enter sorted array elements: ").split()))
k = int(input("Enter value of k: "))
x = int(input("Enter target value x: "))

result = findClosestElements(arr, k, x)

print("K Closest Elements:", result)