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

def validate_symmetric_binary_tree(root):
    depth = depth_of_tree(root, level=1)
    sorted_list = [None] * (pow(2, depth) - 1)
    sorted_list = convert_tree_to_list(root, 0, sorted_list)
    print(sorted_list)

    flag = True
    for level in range(1, depth+1):
        print('level is {}'.format(level))
        start_index = pow(2, level-1) - 1
        end_index = pow(2, level) - 2
        print('start_index and end_index {}, {}'.format(start_index, end_index))
        for i in range((end_index - start_index)/2 + 1):
            if sorted_list[start_index+i] != sorted_list[end_index-i]:
                flag = False
                return flag

    return flag

node31 = Node(3)
node41 = Node(4)
node42 = Node(4)
node32 = Node(3)

node21 = Node(2, node31, node41)
node22 = Node(2, node42, node32)

node1 = Node(1, node21, node22)

n3 = Node(3)
n32 = Node(3)
n2 = Node(2, None, n3)
n22 = Node(2, None, n32)
n1 = Node(1, n2, n22)

print(validate_symmetric_binary_tree(n1))

