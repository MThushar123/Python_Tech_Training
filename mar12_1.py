def search_insert_position(sorted_nums, target):

    for i in range(len(sorted_nums)):
        if sorted_nums[i] >= target:
            return i

    return len(sorted_nums)

print(" Search Insert Position")
print("Enter sorted numbers space separated:")
nums = list(map(int, input().split()))

print("Enter target number:")
target = int(input())

position = search_insert_position(nums, target)

print(f" Target: {target}")
print(f" Insert at index: {position}")

result = nums[:position] + [target] + nums[position:]
print(f"After insert: {result}")
