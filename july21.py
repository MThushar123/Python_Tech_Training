def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

height = list(map(int, input("Enter the heights: ").split()))

result = maxArea(height)

print("Maximum Water Container Area:", result)