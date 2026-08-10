n = int(input("Enter the paatern number"))
i = 0

while i < n:
    space_count = 2 * (n - i - 1)
    j = 0
    while j < space_count:
        print(" ", end="")
        j = j + 1

    star_count = 2 * i + 1
    k = 0
    while k < star_count:
        print("* ", end="")
        k = k + 1

    print()
    i = i + 1
