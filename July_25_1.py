#By using brute force
def longest_substring_length_bruteforce(s):
    max_len = 0
    n = len(s)

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break 
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len

s = "abcabcbb"
print(longest_substring_length_bruteforce(s)) 