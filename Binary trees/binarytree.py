# Depth first values:
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
    nodes = []
    if root is None:
        return nodes
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        nodes.append(current.val)
        if current.right != None:
            stack.append(current.right)
        if current.left != None:
            stack.append(current.left)
    return nodes


def recursive_dfv(root):
    nodes = []
    if root is None:
        return nodes

    right = recursive_dfv(root.right)
    left = recursive_dfv(root.left)

    nodes.append(root.val)
    nodes.extend(left)
    nodes.extend(right)

    return nodes
