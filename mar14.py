def is_valid_parentheses(s):
    """
    Check if brackets match perfectly!
    """
    stack = []  

    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':  
            stack.append(char)  
        elif char in pairs:   
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
        else:
            return False 

    return len(stack) == 0

print("Valid Parentheses Checker")
print("Enter brackets string:")

brackets = input().strip()
result = is_valid_parentheses(brackets)

print(f"'{brackets}' → {' VALID' if result else 'INVALID'}")
