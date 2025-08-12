# 3 Sum - Finding sum of values in array which matches the TARGET

def three_sum(arr,target):
    n = len(arr)
    
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == target:
                    print(arr[i]+arr[j]+arr[k])
                    return True
    return False                
                
arr = [5,2,6,3,4,9,8,1]
target = 15

if three_sum(arr,target):
    print("true")
else:    
    print("False")