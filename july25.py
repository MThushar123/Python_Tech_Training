import math

def canMeasureWater(x, y, target):
    if target > x + y:
        return False

    if target == 0:
        return True

    return target % math.gcd(x, y) == 0

x = int(input("Enter capacity of Jug 1: "))
y = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount of water: "))

result = canMeasureWater(x, y, target)

print("Can measure target water:", result)