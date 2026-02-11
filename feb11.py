def reverse_words(sentence):
    # Split sentence into words
    words = sentence.split()
    # Reverse the order of words
    reversed_words = words[::-1]
    # Join back into sentence
    return ' '.join(reversed_words)

print("Enter a sentence:")
user_input = input().strip()
result = reverse_words(user_input)
print(f"Reversed: {result}")
