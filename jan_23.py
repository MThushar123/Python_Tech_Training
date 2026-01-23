def power(base, exp):
    # Base case: any number raised to the power of 0 is 1
    if exp == 0:
        return 1
    # Recursive case: base * (base raised to exp-1)
    else:
        return base * power(base, exp - 1)

print(power(2, 3))  
print(power(5, 0))  
print(power(3, 4))  