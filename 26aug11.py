def main():

    N = int(input("Enter pattern size-->"))
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print("*", end="")
     
        print()


if __name__ == "__main__":
    main()