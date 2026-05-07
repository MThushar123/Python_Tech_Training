def numPrimeArrangements(n):
    MOD = 10**9 + 7
    
    def factorial(k):
        result = 1
        for i in range(2, k + 1):
            result = (result * i) % MOD
        return result
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
    non_prime_count = n - prime_count

    return (factorial(prime_count) * factorial(non_prime_count)) % MOD

def main():
    n = int(input("Enter n (1 <= n <= 100): ").strip())
    result = numPrimeArrangements(n)
    print(f"Prime arrangements for 1 to {n}: {result}")

if __name__ == "__main__":
    main()