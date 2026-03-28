def is_ugly(n):
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2

    while n % 3 == 0:
        n //= 3

    while n % 5 == 0:
        n //= 5

    return n == 1

print("Ugly Number Checker")
print("Enter number:")
n = int(input().strip())

result = is_ugly(n)
print(f"{n} → {' UGLY!' if result else ' CLEAN!'}")

def show_divisions(n):
    original = n
    steps = []
    
    if n <= 0:
        return ["Negative/Zero → False"]
    
    while n % 2 == 0:
        steps.append(f"{n} ÷ 2 = {n//2}")
        n //= 2
    
    while n % 3 == 0:
        steps.append(f"{n} ÷ 3 = {n//3}")
        n //= 3
    
    while n % 5 == 0:
        steps.append(f"{n} ÷ 5 = {n//5}")
        n //= 5
    
    steps.append(f"Final: {n} → {'Ugly' if n == 1 else 'Not Ugly'}")
    return steps

print("\n Step-by-step:")
for step in show_divisions(int(n)):
    print(f"  {step}")
