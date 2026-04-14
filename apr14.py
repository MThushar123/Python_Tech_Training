def repeated_substring_pattern(s):
    return s in (s + s)[1:-1]
print("Enter the input")
s = input().strip()
print(f'Input: "{s}"')
print(f'Repeated pattern: {repeated_substring_pattern(s)}')