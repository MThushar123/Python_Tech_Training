def findAllConcatenatedWords(words):
    word_set = set(words)
    result = []

    def canForm(word):
        if not word:
            return False

        dp = [False] * (len(word) + 1)
        dp[0] = True

        for i in range(1, len(word) + 1):
            for j in range(i):
                if not dp[j]:
                    continue

                # Prevent using the whole word itself
                if j == 0 and i == len(word):
                    continue

                if word[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(word)]

    for word in words:
        word_set.remove(word)

        if canForm(word):
            result.append(word)

        word_set.add(word)

    return result

words = input("Enter words separated by spaces: ").split()

result = findAllConcatenatedWords(words)

print("Concatenated Words:")
if result:
    for word in result:
        print(word)
else:
    print("No concatenated words found.")