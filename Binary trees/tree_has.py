def tree_has(root, target):
    if root is None:
        return False
    if root.val == target:
        return True

    return tree_has(root.left, target) or tree_has(root.right, target)
