def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    return dp[0][n - 1]

def main():
    s = input("Enter string: ").strip()
    result = longestPalindromeSubseq(s)
    print(f"Longest palindromic subsequence length: {result}")

if __name__ == "__main__":
    main()