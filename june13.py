
def superPow(a, b):
    MOD = 1337

    def modPow(x, n):
        result = 1
        x %= MOD

        while n > 0:
            if n % 2 == 1:
                result = (result * x) % MOD

            x = (x * x) % MOD
            n //= 2

        return result

    def helper(digits):
        if not digits:
            return 1

        last_digit = digits.pop()

        part1 = modPow(helper(digits), 10)
        part2 = modPow(a, last_digit)

        return (part1 * part2) % MOD

    return helper(b[:])  

a = int(input("Enter value of a: "))
b = list(map(int, input("Enter digits of b separated by spaces: ").split()))

result = superPow(a, b)

print("Result:", result)