def my_sqrt(x):
    if x <= 1:
        return x

    left = 1
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid == x:
            return mid  
        elif mid * mid < x:
            left = mid + 1  
        else:
            right = mid - 1  

    return right

print("Square Root Calculator")
print("Enter x:")
x = int(input().strip())

root = my_sqrt(x)
print(f"Check: {root}²={root*root}")
