def print_arrow(n):
    for i in range(1, n):
        for j in range(0, i):
            print(" ", end="")

        for k in range(0, i):
            print("*", end="")

        print()

    for i in range(0, n):
        for j in range(0, n - i):
            print(" ", end="")

        for k in range(0, n - i):
            print("*", end="")

        print()

n = int(input("Enter the value of n: "))

print_arrow(n)