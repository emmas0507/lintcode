class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def depth_of_tree(root):
    if root.left is not None:
        left_depth = depth_of_tree(root.left)
    else:
        left_depth = 0
    if root.right is not None:
        right_depth = depth_of_tree(root.right)
    else:
        right_depth = 0
    return max(left_depth, right_depth) + 1

def convert_tree_to_list(root, index, sorted_list):
    sorted_list[index] = root.value
    if root.left is not None:
        sorted_list = convert_tree_to_list(root.left, 2*index+1, sorted_list)
    if root.right is not None:
        sorted_list = convert_tree_to_list(root.right, 2*index+2, sorted_list)
    return sorted_list

def same_tree(root1, root2):
    depth1 = depth_of_tree(root1)
    depth2 = depth_of_tree(root2)
    if depth1 != depth2:
        return False

    sorted_list1 = [None] * (pow(2, depth1) - 1)
    sorted_list1 = convert_tree_to_list(root1, 0, sorted_list1)

    sorted_list2 = [None] * (pow(2, depth2) - 1)
    sorted_list2 = convert_tree_to_list(root2, 0, sorted_list2)
    print('sorted list 1, {}'.format(sorted_list1))
    print('sorted list 2, {}'.format(sorted_list2))
    for i in range(len(sorted_list1)):
        if sorted_list1[i] != sorted_list2[i]:
            return False

    return True

node2 = Node(2)
node3 = Node(3)
node1 = Node(1, node2, node3)

node22 = Node(2)
node32 = Node(3)
node12 = Node(1, node22, node32)

node23 = Node(2)
node13 = Node(1, node23, None)
node24 = Node(2)
node14 = Node(1, None, node24)
print(same_tree(node1, node12))
print(same_tree(node13, node14))
