from collections import Counter

def commonChars(words):
    if not words:
        return []

    min_freq = Counter(words[0])

    for word in words[1:]:
        word_freq = Counter(word)
        for char in min_freq:
            min_freq[char] = min(min_freq[char], word_freq[char])

    result = []
    for char, freq in min_freq.items():
        result.extend([char] * freq)
    
    return result

def main():
    words_input = input("Enter space-separated words: ").strip().split()
    result = commonChars(words_input)
    print(f"Common characters: {result}")

if __name__ == "__main__":
    main()