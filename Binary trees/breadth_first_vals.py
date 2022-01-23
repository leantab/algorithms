# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):
    nodes = []
    if root is None:
        return nodes

    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        nodes.append(current.val)

        if current.left != None:
            queue.append(current.left)
        if current.right != None:
            queue.append(current.right)

    return nodes
