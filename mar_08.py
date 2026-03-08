class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10           
            reversed_num = reversed_num * 10 + digit  
            x //= 10                 
        
        return original == reversed_num

print("Enter a number to check if it's a palindrome:")

num = int(input().strip())

solution = Solution()
is_pal = solution.isPalindrome(num)

if is_pal:
    print(f" {num} is a PALINDROME!")
else:
    print(f" {num} is NOT a palindrome!")

