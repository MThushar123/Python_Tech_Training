def most_common_word(sentence):
    # Cleaning and spliting into words (lowercase, remove punctuation)
    words = sentence.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
    
    if not words:
        return None
    
    # Counting frequencies by using dictionary
    word_count = {}
    for word in words:
        if word:  # Skip empty strings
            word_count[word] = word_count.get(word, 0) + 1
    
    # Find word with max count
    most_common = max(word_count, key=word_count.get)
    return most_common

# Interactive usage
print("Enter a sentence:")
sentence = input().strip()
result = most_common_word(sentence)
if result:
    print(f"Most common word: '{result}'")
else:
    print("No words found.")
