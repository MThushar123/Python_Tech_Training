def findTargetSumWays(nums, target):
    dp = {0: 1}

    for num in nums:
        new_dp = {}
        for curr_sum, count in dp.items():
            new_dp[curr_sum + num] = new_dp.get(curr_sum + num, 0) + count
            new_dp[curr_sum - num] = new_dp.get(curr_sum - num, 0) + count
        dp = new_dp

    return dp.get(target, 0)

nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target sum: "))

result = findTargetSumWays(nums, target)

print("Number of Ways:", result)