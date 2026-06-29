def flipLights(n, presses):
    n = min(n, 3)

    if presses == 0:
        return 1

    if n == 1:
        if presses >= 1:
            return 2

    elif n == 2:
        if presses == 1:
            return 3
        if presses >= 2:
            return 4

    else:  # n == 3
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        if presses >= 3:
            return 8

    return 1

n = int(input("Enter number of bulbs: "))
presses = int(input("Enter number of presses: "))

result = flipLights(n, presses)

print("Number of Different Possible States:", result)