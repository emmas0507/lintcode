class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tweaked_identical_binary_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None and root1.value == root2.value:
        same_side_equal = tweaked_identical_binary_tree(root1.left, root2.left) and tweaked_identical_binary_tree(root1.right, root2.right)
        diff_side_equal = tweaked_identical_binary_tree(root1.left, root2.right) and tweaked_identical_binary_tree(root1.right, root2.left)
        return same_side_equal or diff_side_equal
    else:
        return False

node4 = Node(4)
node3 = Node(3)
node2 = Node(2, node4, None)
node1 = Node(1, node2, node3)

node42 = Node(4)
node32 = Node(3, node42, None)
node22 = Node(2)
node11 = Node(1, node32, node22)

print(tweaked_identical_binary_tree(node1, node11))
