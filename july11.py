def countSubarrays(nums, bound):
    count = 0
    ans = 0

    for num in nums:
        if num <= bound:
            count += 1
        else:
            count = 0

        ans += count

    return ans


def numSubarrayBoundedMax(nums, left, right):
    return countSubarrays(nums, right) - countSubarrays(nums, left - 1)

nums = list(map(int, input("Enter array elements: ").split()))
left = int(input("Enter left bound: "))
right = int(input("Enter right bound: "))

result = numSubarrayBoundedMax(nums, left, right)

print("Number of Subarrays with Bounded Maximum:", result)