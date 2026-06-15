
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

nums = list(map(int, input("Enter array elements: ").split()))

result = containsDuplicate(nums)

print("Contains Duplicate:", result)