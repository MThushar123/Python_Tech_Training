
def arrangeCoins(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2

        coins_needed = mid * (mid + 1) // 2

        if coins_needed == n:
            return mid
        elif coins_needed < n:
            left = mid + 1
        else:
            right = mid - 1

    return right

n = int(input("Enter number of coins: "))

result = arrangeCoins(n)

print("Number of Complete Rows:", result)