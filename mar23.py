def add_digits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

def show_steps(num):
    current = num  # Track CURRENT number
    steps = []
    
    while current >= 10:
        digit_sum = 0
        temp = current
        
        # Sum all digits
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        
        steps.append(f"{current} → {digit_sum}")
        current = digit_sum  # Update current!
    
    steps.append(f"Final: {current}")
    return steps

# Test it!
print(" Digital Root Calculator")
print("Enter number:")
n = int(input().strip())

result = add_digits(n)
print(f"\n Magic formula: {n} → {result}")

print("\n Manual steps:")
for step in show_steps(n):
    print(f"  {step}")

print(f"\nMatches: {result}")
