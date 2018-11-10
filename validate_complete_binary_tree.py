# count the number of nodes, and then order nodes by their level, from left to right
# to see if all index from 0 to the number of nodes all filled

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def count_number_nodes(root):
    if root is not None:
        return 1 + count_number_nodes(root.left) + count_number_nodes(root.right)
    else:
        return 0

def flatten_binary_tree(root, index, number_node):
    left_ = True
    right_ = True
    if root.left is not None:
        left_ = flatten_binary_tree(root.left, 2*index+1, number_node)
    if root.right is not None:
        right_ = flatten_binary_tree(root.right, 2*index+2, number_node)

    return (index < number_node) and left_ and right_


def validate_complete_binary_tree(root):
    number_nodes = count_number_nodes(root)
    print('number of nodes {}'.format(number_nodes))
    index = 0
    return flatten_binary_tree(root, index, number_nodes)

node4 = Node(4)
node5 = Node(5)
node2 = Node(2, node4, node5)
node3 = Node(3)
node1 = Node(1, node2, node3)

print(validate_complete_binary_tree(node1))
