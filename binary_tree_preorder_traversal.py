def binary_tree_preorder_traversal(atree):
    if atree is None:
        return
    print(atree.value)
    binary_tree_preorder_traversal(atree.left)
    binary_tree_preorder_traversal(atree.right)

class node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

node4 = node(4, None, None)
node5 = node(5, None, None)
node2 = node(2, node4, node5)
node3 = node(3, None, None)
node1 = node(1, node2, node3)

binary_tree_preorder_traversal(node1)
