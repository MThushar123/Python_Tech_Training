def totalHammingDistance(nums):
    n = len(nums)
    total = 0

    for bit in range(32):
        ones = 0

        for num in nums:
            if (num >> bit) & 1:
                ones += 1

        zeros = n - ones
        total += ones * zeros

    return total

nums = list(map(int, input("Enter array elements: ").split()))

result = totalHammingDistance(nums)

print("Total Hamming Distance:", result)