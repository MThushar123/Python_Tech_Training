def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return 
        return num1 / num2
    else:
        return 

# Interactive usage
print("Simple Calculator")
print("Enter first number:")
num1 = float(input())
print("Enter operator (+, -, *, /):")
op = input().strip()
print("Enter second number:")
num2 = float(input())

result = calculator(num1, num2, op)
print(f"Result: {result}")
