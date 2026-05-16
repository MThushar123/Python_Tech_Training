
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next

    return head

def partition(head, x):
    before_head = ListNode(0)
    after_head = ListNode(0)

    before = before_head
    after = after_head

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next

        head = head.next

    after.next = None
    before.next = after_head.next

    return before_head.next

def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

nums = list(map(int, input("Enter linked list elements: ").split()))
x = int(input("Enter partition value x: "))

head = create_linked_list(nums)

new_head = partition(head, x)

print("Partitioned List:")
print_list(new_head)