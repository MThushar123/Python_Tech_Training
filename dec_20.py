def is_balanced(expression):
    stack = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set('([{')
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in matching_brackets:
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()
    
    return not stack

# Get user input
user_input = input("Enter an expression to check for balanced parentheses: ")
if is_balanced(user_input):
    print("The expression has balanced parentheses.")
else:
    print("The expression does not have balanced parentheses.")