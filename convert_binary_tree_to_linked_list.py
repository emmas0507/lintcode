class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def convert_binary_tree_to_linked_list(root):
    head = root
    tail = root
    if root.left is not None:
        left_head, left_tail = convert_binary_tree_to_linked_list(root.left)
        head = left_head
        left_tail.right = root
        root.left = left_tail
    if root.right is not None:
        right_head, right_tail = convert_binary_tree_to_linked_list(root.right)
        tail = right_tail
        right_head.left = root
        root.right = right_head
    return head, tail

def print_linked_list(head):
    while head is not None and head.right is not None:
        print('head.value is {}, head.right is {}, head.right.left is {}'.format(head.value, head.right.value, head.right.left.value))
        head = head.right
    print('head value is {}'.format(head.value))

node25 = Node(25)
node30 = Node(30)
node36 = Node(36)
node15 = Node(15, node36, None)
node12 = Node(12, node25, node30)
node10 = Node(10, node12, node15)

head, tail = convert_binary_tree_to_linked_list(node10)

print_linked_list(head)
