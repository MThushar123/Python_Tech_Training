def first_uniq_char(s):
    if not s:
        return -1

    count = [0] * 26

    for char in s:
        count[ord(char) - ord('a')] += 1

    for i, char in enumerate(s):
        if count[ord(char) - ord('a')] == 1:
            return i
    
    return -1  

print("First Unique Character Finder")
print("Enter string lowercase letters:")

text = input().strip()
index = first_uniq_char(text)

if index == -1:
    print(f"'{text}' →  NO unique chars!")
else:
    print(f"'{text}' → '{text[index]}' at index {index}")
