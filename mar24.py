def plus_one(digits):
    i = len(digits) - 1
    
    while i >= 0:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            i -= 1

    digits.insert(0, 1)
    return digits

print("Plus One Calculator")
print("Enter digits (space separated):")

digits = list(map(int, input().split()))
print(f"Number: {digits}")

result = plus_one(digits)
print(f"Plus 1: {result}")
