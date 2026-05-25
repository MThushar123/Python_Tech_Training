
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next

    return head

def sortList(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(mid)

    return merge(left, right)


def merge(left, right):
    dummy = ListNode(0)
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next

        current = current.next

    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

nums = list(map(int, input("Enter linked list elements: ").split()))

head = createLinkedList(nums)

sorted_head = sortList(head)

print("Sorted Linked List:")
printList(sorted_head)