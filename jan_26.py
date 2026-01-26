def binary_to_decimal(binary):
    decimal = 0
    power = 1  # Start with 2^0
    for bit in reversed(binary):  # Iterate from least significant bit
        if bit == '1':
            decimal += power
        power *= 2  # Multiply by 2 for next power
    return decimal

print(binary_to_decimal("1001"))  