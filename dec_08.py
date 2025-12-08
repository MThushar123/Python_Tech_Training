#Median of Sliding Window 

from heapq import *
from collections import defaultdict
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or k == 0:
            return []
        
        small = []  # max-heap (using negatives)
        large = []  # min-heap
        removed = defaultdict(int)
        
        def add(num):
            if not small or num <= -small[0]:
                heappush(small, -num)
            else:
                heappush(large, num)
            balance()
        
        def remove(num):
            removed[num] += 1
            balance()
        
        def balance():
            # Clean up removed elements
            while small and removed[-small[0]] > 0:
                removed[-small[0]] -= 1
                heappop(small)
            while large and removed[large[0]] > 0:
                removed[large[0]] -= 1
                heappop(large)
            # Balance sizes
            if len(small) > len(large) + 1:
                heappush(large, -heappop(small))
            elif len(large) > len(small):
                heappush(small, -heappop(large))
        
        def get_median():
            if k % 2 == 1:
                return -small[0]
            else:
                return (-small[0] + large[0]) / 2
        
        result = []
        for i in range(len(nums)):
            add(nums[i])
            if i >= k - 1:
                result.append(get_median())
                remove(nums[i - k + 1])
        
        return result

# Main block to take user input and run the code
if __name__ == "__main__":
    # Take input for nums (list of integers)
    nums_input = input("Enter the list of numbers (space-separated, e.g., 1 3 -1 -3 5 3 6 7): ")
    nums = list(map(int, nums_input.split()))
    
    # Take input for k (window size)
    k = int(input("Enter the window size k (e.g., 3): "))
    
    # Instantiate the class and call the method
    solution = Solution()
    result = solution.medianSlidingWindow(nums, k)
    
    # Print the output

    print("Medians for each sliding window:", result)