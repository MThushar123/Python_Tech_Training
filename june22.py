def countBits(n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)

    return dp

n = int(input("Enter a non-negative integer: "))

result = countBits(n)

print("Number of 1's in binary representation from 0 to", n)
print(result)