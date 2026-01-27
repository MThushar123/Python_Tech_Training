string = input("Enter a string: ")

# Initialize counters
vowel_count = 0
consonant_count = 0

# Define vowels (both lowercase and uppercase)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Iterate through each character in the string
for char in string:
    # Check if the character is an alphabetic letter (a-z or A-Z)
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        # Check if it's a vowel
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)