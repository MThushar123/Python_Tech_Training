def bestRotation(nums):
    n = len(nums)
    change = [0] * (n + 1)

    for i in range(n):
        left = (i - nums[i] + 1 + n) % n
        right = (i + 1) % n

        change[left] -= 1
        change[right] += 1

        if left > right:
            change[0] -= 1

    best = 0
    score = 0
    max_score = -n

    for k in range(n):
        score += change[k]
        current_score = score + n
        if current_score > max_score:
            max_score = current_score
            best = k

    return best

nums = list(map(int, input("Enter array elements: ").split()))

result = bestRotation(nums)

print("Smallest Rotation with Highest Score:", result)