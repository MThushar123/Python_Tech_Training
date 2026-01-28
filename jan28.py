def longest_common_prefix(strings):
    if not strings:
        return ""
    
    # Take the shortest string as reference
    min_len = min(len(s) for s in strings)
    
    for i in range(min_len):
        char = strings[0][i]
        if any(s[i] != char for s in strings[1:]):
            return strings[0][:i]
    
    return strings[0][:min_len]

print("Enter strings separated by commas:")
user_input = input().strip()
if user_input:
    string_list = [s.strip() for s in user_input.split(',')]
    result = longest_common_prefix(string_list)
    print(f"Longest common prefix: '{result}'")
else:
    print("No input provided.")
