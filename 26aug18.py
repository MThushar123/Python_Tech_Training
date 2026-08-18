def hollowSquare(rows):

    for i in range(rows):
        for j in range(rows):

            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                print("*", end="")
            else:
                print(" ", end="")

        print()


def solidSquare(rows):

    for i in range(rows):
        print("*" * rows)


def printPattern(rows):

    print("Solid Square:")
    solidSquare(rows)

    print("\nHollow Square:")
    hollowSquare(rows)


rows = int(input("Enter the number of rows: "))

printPattern(rows)