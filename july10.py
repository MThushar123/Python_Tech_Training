from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root

def isCousins(root, x, y):
    queue = deque([(root, None)])  # (node, parent)

    while queue:
        size = len(queue)
        x_parent = None
        y_parent = None

        for _ in range(size):
            node, parent = queue.popleft()

            if node.val == x:
                x_parent = parent

            if node.val == y:
                y_parent = parent

            if node.left:
                queue.append((node.left, node))

            if node.right:
                queue.append((node.right, node))

        if x_parent and y_parent:
            return x_parent != y_parent

        if x_parent or y_parent:
            return False

    return False

values = input("Enter tree in level order (use 'null' for empty nodes): ").split()
x = int(input("Enter first node value: "))
y = int(input("Enter second node value: "))

root = buildTree(values)

result = isCousins(root, x, y)

print("Are Cousins:", result)