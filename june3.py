def calculate(s):
    stack = []
    num = 0
    sign = 1
    result = 0

    i = 0
    while i < len(s):
        char = s[i]

        if char.isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            result += sign * num
            continue

        elif char == '+':
            sign = 1

        elif char == '-':
            sign = -1

        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1

        elif char == ')':
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result = prev_result + prev_sign * result

        i += 1

    return result

expression = input("Enter expression: ")

result = calculate(expression)

print("Result:", result)