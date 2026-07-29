def rob(nums):
    prev2 = 0  
    prev1 = 0  

    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current

    return prev1

nums = list(map(int, input("Enter money in each house: ").split()))

result = rob(nums)

print("Maximum Money That Can Be Robbed:", result)