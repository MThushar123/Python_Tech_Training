def main():
    N = int(input("Enter the number of rows: "))

    for i in range(1, N + 1):
        for _ in range(i - 1):
            print("  ", end="")

        for _ in range(N - i + 1):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()