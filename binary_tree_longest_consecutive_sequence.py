class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_longest_consecutive_sequence(root):
    cl_list = consecutive_path(root, cl=1, cl_list=[])
    return max(cl_list)

def consecutive_path(root, cl=1, cl_list=[]):
    cl_list = cl_list + [cl]
    if root.left is not None:
        if root.left.value == root.value + 1:
            left_cl = cl + 1
        else:
            left_cl = 1
        cl_list = consecutive_path(root.left, cl=left_cl, cl_list=cl_list)
    if root.right is not None:
        if root.right.value == root.value + 1:
            right_cl = cl + 1
        else:
            right_cl = 1
        cl_list = consecutive_path(root.right, cl=right_cl, cl_list=cl_list)
    return cl_list

n2 = Node(2)
n5 = Node(5)
n4 = Node(4, None, n5)
n3 = Node(3, n2, n4)
n1 = Node(1, None, n3)

print(binary_tree_longest_consecutive_sequence(n1))
