# Find Median of Two Sorted Arrays 

def median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    
    if n % 2 == 0:
        median = (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        median = merged[n // 2]
    
    return median

nums1 = list(map(int, input("Enter the elements of the first sorted array (space-separated): ").split()))
nums2 = list(map(int, input("Enter the elements of the second sorted array (space-separated): ").split()))

median = median_sorted_arrays(nums1, nums2)
print("The median of the two sorted arrays is:", median)
