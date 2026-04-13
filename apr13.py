def number_complement(num):
    bit_length = num.bit_length()
    mask = (1 << bit_length) - 1
    return num ^ mask
print("Enter the number")
num = int(input().strip())
print(f'Input: {num}')
print(f'Binary: {bin(num)[2:]}')
print(f'Complement: {number_complement(num)}')