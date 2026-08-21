def display_pattern(n):
    width = n // 2 + 1

    for row in range(n):
        for col in range(width):
            if row in (0, n // 2) or col in (0, width - 1):
                if row == 0 and col in (0, width - 1):
                    print(" ", end="")
                else:
                    print("*", end="")
            else:
                print(" ", end="")
        print()


number = int(input("Enter the number: "))
display_pattern(number)