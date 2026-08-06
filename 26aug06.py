def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    memo = {}

    def dfs(start):
        if start in memo:
            return memo[start]

        if start == len(s):
            return [""]

        result = []

        for end in range(start + 1, len(s) + 1):
            word = s[start:end]

            if word in wordSet:
                suffixes = dfs(end)

                for suffix in suffixes:
                    if suffix:
                        result.append(word + " " + suffix)
                    else:
                        result.append(word)

        memo[start] = result
        return result

    return dfs(0)

s = input("Enter the string: ")
wordDict = input("Enter dictionary words (space-separated): ").split()

result = wordBreak(s, wordDict)

print("Possible Sentences:")
if result:
    for sentence in result:
        print(sentence)
else:
    print("No valid sentence can be formed.")