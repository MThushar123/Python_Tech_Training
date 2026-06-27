class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self.data = []
        else:
            self.data = value

    def __repr__(self):
        return str(self.data)


def deserialize(s):
    if s[0] != '[':
        return NestedInteger(int(s))

    stack = []
    num = ""
    negative = False

    for ch in s:
        if ch == '-':
            negative = True

        elif ch.isdigit():
            num += ch

        elif ch == '[':
            stack.append(NestedInteger())

        elif ch == ',' or ch == ']':
            if num:
                value = int(num)
                if negative:
                    value = -value

                stack[-1].data.append(value)
                num = ""
                negative = False

            if ch == ']' and len(stack) > 1:
                last = stack.pop()
                stack[-1].data.append(last.data)

    return stack.pop()

s = input("Enter nested integer string: ")

result = deserialize(s)

print("Parsed Nested Integer:")
print(result)