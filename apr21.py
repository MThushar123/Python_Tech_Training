def reverse_string_ii(s, k):
    chars = list(s)
    n = len(chars)
    
    for i in range(0, n, 2 * k):
        chars[i:i+k] = chars[i:i+k][::-1]
    
    return ''.join(chars)
print("Enter the string")
s = input("Enter s: ").strip()
k = int(input("Enter k: ").strip())
print(f's="{s}", k={k}')
print(f'Result: "{reverse_string_ii(s, k)}"')