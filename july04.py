def findContentChildren(g, s):
    # Sort greed factors and cookie sizes
    g.sort()
    s.sort()

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1

    return child

g = list(map(int, input("Enter children's greed factors: ").split()))
s = list(map(int, input("Enter cookie sizes: ").split()))

result = findContentChildren(g, s)

print("Maximum Content Children:", result)