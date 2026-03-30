def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1 
        count += 1
    return count

print(" Count 1 Bits (Binary)")
print("Enter number (decimal):")
n = int(input().strip())

ones = hamming_weight(n)
binary = bin(n)[2:]  

print(f"n={n}")
print(f"Binary: {binary}")
print(f"1s: {ones}")