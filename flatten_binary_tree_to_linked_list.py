class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def flatten_binary_tree_to_linked_list(root):
    tail = root
    if root.left is not None:  # get left flatten list
        flatten_left_head, flatten_left_tail = flatten_binary_tree_to_linked_list(root.left)
    else:
        flatten_left_head = None
        flatten_left_tail = None
    if root.right is not None:  # get right flatten list
        flatten_right_head, flatten_right_tail = flatten_binary_tree_to_linked_list(root.right)
    else:
        flatten_right_head = None
        flatten_right_tail = None

    if flatten_left_head is not None:
        tail.right = flatten_left_head
        tail = flatten_left_tail
    if flatten_right_head is not None:
        tail.right = flatten_right_head
        tail = flatten_right_tail
    return root, tail

def print_list(root):
    print('the list is:')
    while root is not None:
        print(root.value)
        root = root.right

node3 = Node(3)
node4 = Node(4)
node6 = Node(6)

node2 = Node(2, node3, node4)
node5 = Node(5, None, node6)

node1 = Node(1, node2, node5)

print_list(flatten_binary_tree_to_linked_list(node1)[0])

