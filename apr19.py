def detect_capital(word):
    if not word:
        return True
    return (word.isupper() or 
            word.islower() or 
            (word[0].isupper() and word[1:].islower()))
print("Enter the word")
word = input().strip()
print(f'Input: "{word}"')
print(f'Valid capital: {detect_capital(word)}')