class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(values):
    if not values or values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root


def longestUnivaluePath(root):
    max_path = 0

    def dfs(node):
        nonlocal max_path
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        left_path = 0
        right_path = 0

        if node.left and node.left.val == node.val:
            left_path = left + 1

        if node.right and node.right.val == node.val:
            right_path = right + 1

        max_path = max(max_path, left_path + right_path)

        return max(left_path, right_path)

    dfs(root)
    return max_path

values = input(
    "Enter tree nodes in level order (use 'null' for missing nodes): "
).split()

root = buildTree(values)

result = longestUnivaluePath(root)

print("Longest Univalue Path:", result)