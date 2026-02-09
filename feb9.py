def permutations(s):
    """Generate all unique permutations of a string using recursion."""
    if len(s) <= 1:
        return [s]
    
    result = []
    for i in range(len(s)):
        first = s[i]
        remaining = s[:i] + s[i+1:]
        for p in permutations(remaining):
            result.append(first + p)
    
    return result

print("Enter a string:")
user_input = input().strip()
perms = permutations(user_input)
print(f"All permutations ({len(perms)} total):")
for perm in perms:
    print(perm)
