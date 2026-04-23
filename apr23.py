def array_partition(nums):
    nums.sort()
    return sum(nums[::2])
print("ENter the number")
nums = list(map(int, input().strip().split()))
print(f'Input: {nums}')
print(f'Max pair sum: {array_partition(nums)}')