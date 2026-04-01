def guess(num):
    secret = 6  
    if num == secret:
        return 0
    return -1 if num > secret else 1

class Solution:
    def guessNumber(self, n):
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2  # Avoid overflow
            
            result = guess(mid)
            if result == 0:
                return mid  # Found it!
            elif result == 1:
                left = mid + 1  
            else:  # -1
                right = mid - 1  
        
        return -1  

# Interactive Demo
print(" Guess Number Game (1 to n)")
print("Enter n (upper limit):")
n = int(input().strip())

solution = Solution()
answer = solution.guessNumber(n)

print(f"\n Secret number between 1-{n}: **{answer}**")
print("Verified with guess():", guess(answer))