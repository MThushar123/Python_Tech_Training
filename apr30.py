def findAndReplacePattern(words, pattern):
    def get_pattern(word):
        mapping = {}
        reverse_mapping = {}
        pattern_result = []
        next_char = 'a'
        
        for char in word:
            if char not in mapping:
                if next_char > 'z':
                    return None
                mapping[char] = next_char
                reverse_mapping[next_char] = char
                next_char = chr(ord(next_char) + 1)
            pattern_result.append(mapping[char])
        
        return ''.join(pattern_result)
    
    pattern_key = get_pattern(pattern)
    result = []
    
    for word in words:
        if get_pattern(word) == pattern_key:
            result.append(word)
    
    return result

def main():
    words_input = input("Enter space-separated words: ").strip().split()
    pattern = input("Enter pattern: ").strip()
    
    result = findAndReplacePattern(words_input, pattern)
    print(f"Matching words: {result}")

if __name__ == "__main__":
    main()