def longest_palindrome(s):
    count = [0] * 128  # ASCII chars
 
    for char in s:
        count[ord(char)] += 1
    
    length = 0
    has_odd = False

    for freq in count:
        length += (freq // 2) * 2  # Take pairs
        if freq % 2 == 1:
            has_odd = True

    if has_odd:
        length += 1
    
    return length

print(" Longest Palindrome Length")
print("Enter string:")
s = input().strip()

result = longest_palindrome(s)
print(f"'{s}' -> Max palindrome length: {result}")
