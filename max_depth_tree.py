def max_depth_tree(root):
    if root is None:
        return 0
    else:
        return max(max_depth_tree(root.left), max_depth_tree(root.right)) + 1


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


node5 = Node(5)
node4 = Node(4)
node3 = Node(3, node5, node4)
node2 = Node(2)
node1 = Node(1, node2, node3)

print(max_depth_tree(node1))
