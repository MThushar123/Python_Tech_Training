def numberOfArithmeticSlices(nums):
    n = len(nums)
    if n < 3:
        return 0
    
    dp = [0] * n
    total = 0
    
    for i in range(2, n):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            dp[i] = dp[i-1] + 1
            total += dp[i]
    
    return total

def main():
    arr_input = input("Enter space-separated numbers: ").strip().split()
    nums = [int(x) for x in arr_input]
    
    result = numberOfArithmeticSlices(nums)
    print(f"Arithmetic slices: {result}")

if __name__ == "__main__":
    main()