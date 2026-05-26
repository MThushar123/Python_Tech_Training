
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

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

def findNode(head, value):
    current = head

    while current:
        if current.val == value:
            return current
        current = current.next

    return None

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

nums = list(map(int, input("Enter linked list elements: ").split()))
value = int(input("Enter node value to delete: "))

head = createLinkedList(nums)

node_to_delete = findNode(head, value)

if node_to_delete and node_to_delete.next:
    deleteNode(node_to_delete)
    print("Linked List after deletion:")
    printList(head)
else:
    print("Cannot delete this node (last node or not found).")