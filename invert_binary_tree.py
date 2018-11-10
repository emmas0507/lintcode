def invert_binary_tree(root):
    if root is None:
        return None
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return None

def print_tree(root):
    if root is not None:
        print(root.value)
        print_tree(root.left)
        print_tree(root.right)

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

node4 = Node(4)
node3 = Node(3, node4, None)
node2 = Node(2)
node1 = Node(1, node2, node3)
print_tree(node1)

invert_binary_tree(node1)

print_tree(node1)
