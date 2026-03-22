def is_power_of_three(n):

    if n <= 0:
        return False
    
    original = n
    steps = []
    
    while n > 1:
        if n % 3 != 0:
            steps.append(f"{n} % 3 ≠ 0 → False")
            return False, steps
        n = n // 3
        steps.append(f"{original} ÷ 3 = {n}")
    
    steps.append("n == 1 → True!")
    return n == 1, steps

print(" Power of Three Checker")
print("Enter number:")
n = int(input().strip())

result, trace = is_power_of_three(n)
print(f"\n {n} → {'YES' if result else ' NO'}")
