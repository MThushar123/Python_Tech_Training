def printdiamond(n):

    space = n - 1
    for i in range(0, n):
        for j in range(0, space):
            print(" ", end="")
        for j in range(0, i + 1):
            print("* ", end="")

        print()
        space -= 1

    space = 0
    for i in range(n, 0, -1):

        for j in range(0, space):
            print(" ", end="")

        for j in range(0, i):
            print("* ", end="")

        print()
        space += 1

def main():
    printdiamond(5)


if __name__ == "__main__":
    main()