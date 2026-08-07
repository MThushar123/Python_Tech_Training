def superEggDrop(k, n):

    dp = [0] * (k + 1)
    moves = 0

    while dp[k] < n:
        moves += 1

        for eggs in range(k, 0, -1):
            dp[eggs] = dp[eggs] + dp[eggs - 1] + 1

    return moves

k = int(input("Enter number of eggs: "))
n = int(input("Enter number of floors: "))

result = superEggDrop(k, n)

print("Minimum Moves Required:", result)