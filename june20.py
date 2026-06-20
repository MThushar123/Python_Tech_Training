
def isAdditiveNumber(num):

    def valid(first, second, remaining):
        while remaining:
            third = str(int(first) + int(second))

            if not remaining.startswith(third):
                return False

            remaining = remaining[len(third):]
            first, second = second, third

        return True

    n = len(num)

    for i in range(1, n):
        for j in range(i + 1, n):

            first = num[:i]
            second = num[i:j]

            if (len(first) > 1 and first[0] == '0') or \
               (len(second) > 1 and second[0] == '0'):
                continue

            if valid(first, second, num[j:]):
                return True

    return False

num = input("Enter a numeric string: ")

result = isAdditiveNumber(num)

print("Is Additive Number:", result)