from collections import Counter
def single_number_xOR(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(" Single Number Finder")
print("Enter numbers (one appears once):")
nums = list(map(int, input().split()))

print(f"Input: {nums}")
single = single_number_xOR(nums)
print(f" Single: {single}")
