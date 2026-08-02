def isRectangleOverlap(rec1, rec2):
    return (
        rec1[0] < rec2[2] and
        rec1[2] > rec2[0] and
        rec1[1] < rec2[3] and
        rec1[3] > rec2[1]
    )

rec1 = list(map(int, input("Enter Rectangle 1 (x1 y1 x2 y2): ").split()))
rec2 = list(map(int, input("Enter Rectangle 2 (x1 y1 x2 y2): ").split()))

result = isRectangleOverlap(rec1, rec2)

print("Do the rectangles overlap?", result)