def sequentialDigits(low, high):
    result = []
    digits = "123456789"

    for length in range(len(str(low)), len(str(high)) + 1):
        for start in range(0, 10 - length):
            num = int(digits[start:start + length])
            if low <= num <= high:
                result.append(num)

    return result

low = int(input("Enter the lower limit: "))
high = int(input("Enter the upper limit: "))

result = sequentialDigits(low, high)

print("Sequential Digits:", result)