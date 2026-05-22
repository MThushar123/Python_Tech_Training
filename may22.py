
def subsets(nums):
    result = [[]]

    for num in nums:
        new_subsets = [curr + [num] for curr in result]
        result.extend(new_subsets)

    return result

nums = list(map(int, input("Enter array elements: ").split()))

result = subsets(nums)

print("Subsets are:")
for subset in result:
    print(subset)