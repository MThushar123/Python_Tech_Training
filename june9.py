def divide(dividend, divisor):
    # Handle overflow case
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    while dividend >= divisor:
        temp = divisor
        multiple = 1

        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1

        dividend -= temp
        quotient += multiple

    return sign * quotient

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

if divisor == 0:
    print("Division by zero is not allowed.")
else:
    result = divide(dividend, divisor)
    print("Quotient:", result)