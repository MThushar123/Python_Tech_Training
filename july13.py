def toLowerCase(s):
    result = ""

    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch

    return result

s = input("Enter a string: ")

result = toLowerCase(s)

print("Lowercase String:", result)