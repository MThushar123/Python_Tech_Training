def countCharacters(words, chars):
    char_count = {}
    for char in chars:
        char_count[char] = char_count.get(char, 0) + 1
    
    total_length = 0
    for word in words:
        word_count = {}
        can_form = True
        
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1
        
        for char, count in word_count.items():
            if char not in char_count or count > char_count[char]:
                can_form = False
                break
        
        if can_form:
            total_length += len(word)
    
    return total_length

def main():
    words_input = input("Enter space-separated words: ").strip().split()
    chars = input("Enter available chars: ").strip()
    
    result = countCharacters(words_input, chars)
    print(f"Total length of valid words: {result}")

if __name__ == "__main__":
    main()