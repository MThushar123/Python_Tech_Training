def hIndex(citations):
    citations.sort(reverse=True)

    h = 0

    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break

    return h

citations = list(map(int, input("Enter citation counts: ").split()))

result = hIndex(citations)

print("H-Index:", result)