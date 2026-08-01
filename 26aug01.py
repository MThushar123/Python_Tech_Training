def uncommonFromSentences(s1, s2):
    freq = {}

    for word in s1.split():
        freq[word] = freq.get(word, 0) + 1

    for word in s2.split():
        freq[word] = freq.get(word, 0) + 1

    result = []
    for word in freq:
        if freq[word] == 1:
            result.append(word)

    return result

s1 = input("Enter first sentence: ")
s2 = input("Enter second sentence: ")

result = uncommonFromSentences(s1, s2)

print("Uncommon Words:", result)