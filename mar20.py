class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None  # Previous node
        curr = head  # Current node
        
        while curr:
            next_temp = curr.next
            curr.next = prev 
            prev = curr
            curr = next_temp
        
        return prev  

def demo_reverse():
    print(" Reverse Linked List Demo")
    print("Enter list space separated:")
    
    arr = list(map(int, input().split()))
    print(f"Original: {arr}")
    
    reversed_arr = arr[::-1]
    print(f"Reversed: {reversed_arr}")

demo_reverse()
