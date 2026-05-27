
def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result

nums = list(map(int, input("Enter array elements: ").split()))

result = singleNumber(nums)

print("Single Number:", result)