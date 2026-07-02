def integerBreak(n):
    # Base cases
    if n == 2:
        return 1
    if n == 3:
        return 2

    product = 1

    while n > 4:
        product *= 3
        n -= 3

    product *= n
    return product

n = int(input("Enter an integer: "))

result = integerBreak(n)

print("Maximum Product:", result)