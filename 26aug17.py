def printHollowRect(n, m):
    i = 1
    while i <= n:
        j = 1
        while j <= m:
            if i == 1 or i == n or j == 1 or j == m:
                print("*", end="")
            else:
                print(" ", end="")
            j += 1
        print()
        i += 1

if __name__ == '__main__':
    n = int(input("Enter the breadth-->"))
    m = int(input("Enter the length-->"))
    printHollowRect(n, m)