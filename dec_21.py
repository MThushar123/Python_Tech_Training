def gcd(a, b):
    """Compute GCD using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    """Compute LCM using GCD."""
    g = gcd(a, b)
    if g == 0:          # if both numbers are 0, LCM is undefined
        return 0
    return abs(a * b) // g


def get_int(prompt):
    """Safely read an integer from user."""
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input, please enter an integer.")


def main():
    print("GCD and LCM calculator for two integers")
    a = get_int("Enter first integer: ")
    b = get_int("Enter second integer: ")

    g = gcd(a, b)
    l = lcm(a, b)

    print(f"GCD of {a} and {b} is: {g}")
    print(f"LCM of {a} and {b} is: {l}")


if __name__ == "__main__":
    main()
