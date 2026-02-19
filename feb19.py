def rob(houses):
    n = len(houses)
    if n == 0: return 0
    if n == 1: return houses[0]
    if n == 2: return max(houses[0], houses[1])

    prev2 = houses[0]      # Max up to house 0
    prev1 = max(houses[0], houses[1])  # Max up to house 1
    
    for i in range(2, n):
        current = max(
            prev1,                    # Skiping current house
            houses[i] + prev2         # Rob current + skiping prev house
        )
        prev2 = prev1
        prev1 = current
    
    return prev1

houses = [2, 7, 9, 3, 1]
print(f"Max money: {rob(houses)}")  
