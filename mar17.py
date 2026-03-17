def majority_element(nums):

    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num  
        count += 1 if num == candidate else -1
    
    return candidate

print(" Majority Element Finder")
print("Enter numbers (space separated):")

numbers = list(map(int, input().split()))
print(f"Input: {numbers}")

majority = majority_element(numbers)
print(f" Majority: {majority}")

