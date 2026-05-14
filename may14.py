def integerReplacement(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            if n % 4 == 3 and n > 3:
                n += 1
            else:
                n -= 1
        count += 1
    return count

def main():
    n = int(input("Enter positive integer n: ").strip())
    result = integerReplacement(n)
    print(f"Minimum replacements: {result}")

if __name__ == "__main__":
    main()