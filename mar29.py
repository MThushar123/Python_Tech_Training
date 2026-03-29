def length_of_last_word(s):
    i = len(s) - 1  # Start at end
    length = 0

    while i >= 0 and s[i] == ' ':
        i -= 1

    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    
    return length

print(" Length of Last Word")
print("Enter string:")
text = input().strip('"\'')  # Remove quotes if any

result = length_of_last_word(text)
print(f"'{text}' -> Last word length: {result}")