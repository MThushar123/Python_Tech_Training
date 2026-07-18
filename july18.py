def palindromePairs(words):
    word_map = {word: i for i, word in enumerate(words)}
    result = []

    def isPalindrome(s):
        return s == s[::-1]

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]

            if isPalindrome(prefix):
                rev = suffix[::-1]
                if rev in word_map and word_map[rev] != i:
                    result.append([word_map[rev], i])

            if j != len(word) and isPalindrome(suffix):
                rev = prefix[::-1]
                if rev in word_map and word_map[rev] != i:
                    result.append([i, word_map[rev]])

    return result

words = input("Enter words separated by spaces: ").split()

result = palindromePairs(words)

print("Palindrome Pairs:")
if result:
    for pair in result:
        print(pair)
else:
    print("No palindrome pairs found.")