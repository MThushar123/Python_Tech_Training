def findErrorNums(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    duplicate = sum(xi * xi for xi in nums) - (n * (n + 1) * (2 * n + 1) // 6)
    
    missing = total_sum - actual_sum
    duplicate = duplicate // (2 * missing)
    
    return [duplicate, missing]

def main():
    nums_input = input("Enter space-separated numbers: ").strip().split()
    nums = [int(x) for x in nums_input]
    
    result = findErrorNums(nums)
    print(f"Duplicate: {result[0]}, Missing: {result[1]}")

if __name__ == "__main__":
    main()