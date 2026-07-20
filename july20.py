def convertToBase7(num):
    if num == 0:
        return "0"

    negative = num < 0
    num = abs(num)

    result = ""

    while num > 0:
        remainder = num % 7
        result = str(remainder) + result
        num //= 7

    if negative:
        result = "-" + result

    return result

num = int(input("Enter an integer: "))

result = convertToBase7(num)

print("Base 7 Representation:", result)