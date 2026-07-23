class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


def reorderList(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow.next
    slow.next = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first = head
    second = prev

    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2

    return head

arr = list(map(int, input("Enter linked list elements: ").split()))

head = createLinkedList(arr)

head = reorderList(head)

print("Reordered List:")
printLinkedList(head)