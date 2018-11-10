def binary_tree_path_sum(root, target, path, path_list):
    if root is not None and root.left is None and root.right is None:
        if root.value == target:
            print('root is None, path_list is {}'.format(path_list + [path+[root.value]]))
            return [path+[root.value]]
        else:
            return [None]
    else:
        updated_path = path + [root.value]
        print('updated_path is {}'.format(updated_path))
        if root.left is not None:
            left_return_path = binary_tree_path_sum(root.left, target-root.value, updated_path, path_list)
        if root.right is not None:
            right_return_path = binary_tree_path_sum(root.right, target-root.value, updated_path, path_list)
        print('root is {}, left_return_path is {}, right_return_path is {}'.format(root.value, left_return_path, right_return_path))
        return left_return_path + right_return_path

class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

node2 = Node(2)
node3 = Node(3)
node22 = Node(2, node2, node3)
node4 = Node(4)
node1 = Node(1, node22, node4)

path_list = binary_tree_path_sum(node1, target=5, path=[], path_list=[])
print(path_list)
