class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_path_sum_2(node, target, parents_list):
    print('node.value is {}, target is {}'.format(node.value, target))
    if node.value == target:
        print(parents_list + [node.value])
    if node.left is not None:
        print('node.left is {}'.format(node.left.value))
        binary_tree_path_sum_2(node.left, target - node.value, parents_list + [node.value])
    if node.right is not None:
        binary_tree_path_sum_2(node.right, target - node.value, parents_list + [node.value])
    return None

node1 = Node(1)
node2 = Node(2)
node7 = Node(7)
node5 = Node(5)

node11 = Node(11, node7, node2)
node13 = Node(13)
node4 = Node(4, node5, node1)

node41 = Node(4, node11)
node8 = Node(8, node13, node4)

node51 = Node(5, node41, node8)

parents_list = []
target = 22

binary_tree_path_sum_2(node51, target, parents_list)
