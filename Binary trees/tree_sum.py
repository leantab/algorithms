# Binary tree sum all values in nodes

def tree_sum(root):
    if root is None:
        return 0

    count = root.val
    count += tree_sum(root.right)
    count += tree_sum(root.left)

    return count
