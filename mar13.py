class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):

        p1 = headA
        p2 = headB

        while p1 != p2:
            p1 = p1.next if p1 else headB  # End? Jump to other!
            p2 = p2.next if p2 else headA
        
        return p1  
    
def simulate_intersection(list1, list2, intersect_index):

    common = list1[intersect_index:] if intersect_index < len(list1) else []
    
    print(f"List A: {list1}")
    print(f"List B: {list2}")
    print(f"Common: {common}")

    i, j = 0, 0
    steps = 0
    print("\nTwo Pointer Walk:")
    
    while i < len(list1) or j < len(list2):
        print(f"Step {steps}: A[{i}]={list1[i] if i<len(list1) else 'END→B'}, B[{j}]={list2[j] if j<len(list2) else 'END→A'}")
        
        if i < len(list1):
            i += 1
        else:
            i = 0  
        
        if j < len(list2):
            j += 1
        else:
            j = 0  
        
        steps += 1

        if i >= intersect_index and j >= len(list2) - len(common):
            print(f"MEET at common part!")
            break

print("=== Linked List Intersection Demo ===")
listA = [4,1,8,4,5]  # A
listB = [5,6,1,8,4,5]  # B
intersect = 2  

simulate_intersection(listA, listB, intersect)
