def word_pattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}
    
    for p_char, w in zip(pattern, words):
        if p_char in char_to_word and char_to_word[p_char] != w:
            return False
 
        if w in word_to_char and word_to_char[w] != p_char:
            return False

        char_to_word[p_char] = w
        word_to_char[w] = p_char
    
    return True

print(" Word Pattern Matcher")
print("Enter pattern (letters):")
pattern = input().strip()

print("Enter string:")
s = input().strip()

result = word_pattern(pattern, s)
print(f"\nPattern: '{pattern}'")
print(f"String:  '{s}'")
print(f"Match:   {' YES' if result else ' NO'}")