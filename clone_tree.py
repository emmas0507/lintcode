class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def clone_subtree(root, new_root):
    if root.left is not None:
        new_left = Node(root.left.value)
        new_root.left = new_left
        clone_subtree(root.left, new_left)
    if root.right is not None:
        new_right = Node(root.right.value)
        new_root.right = new_right
        clone_subtree(root.right, new_right)

def clone_tree(root):
    new_root = Node(root.value)
    clone_subtree(root, new_root)
    return new_root

def print_tree(root):
    if root is None:
        return
    else:
        print('root value is {}'.format(root.value))
        print_tree(root.left)
        print_tree(root.right)

node4 = Node(4)
node5 = Node(5)
node2 = Node(2, node4, node5)
node3 = Node(3)
node1 = Node(1, node2, node3)

new_node = clone_tree(node1)

print_tree(new_node)
