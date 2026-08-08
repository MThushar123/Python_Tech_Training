def oddEvenJumps(arr):
    n = len(arr)

    if n == 0:
        return 0

    # next_higher[i] = index to jump to on an odd jump
    # next_lower[i]  = index to jump to on an even jump
    next_higher = [None] * n
    next_lower = [None] * n

    sorted_indices = sorted(range(n), key=lambda i: (arr[i], i))

    stack = []
    for i in sorted_indices:
        while stack and i > stack[-1]:
            next_higher[stack.pop()] = i
        stack.append(i)

    sorted_indices = sorted(range(n), key=lambda i: (-arr[i], i))

    stack = []
    for i in sorted_indices:
        while stack and i > stack[-1]:
            next_lower[stack.pop()] = i
        stack.append(i)

    # odd_good[i] = can reach the end if next jump is odd
    # even_good[i] = can reach the end if next jump is even
    odd_good = [False] * n
    even_good = [False] * n

    odd_good[n - 1] = True
    even_good[n - 1] = True

    for i in range(n - 2, -1, -1):

        if next_higher[i] is not None:
            odd_good[i] = even_good[next_higher[i]]

        if next_lower[i] is not None:
            even_good[i] = odd_good[next_lower[i]]

    return sum(odd_good)

arr = list(map(int, input("Enter array elements: ").split()))

result = oddEvenJumps(arr)

print("Number of Good Starting Indices:", result)