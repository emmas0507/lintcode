class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_paths(root, path, allpaths):
    path = path + [root.value]
    if root.left is not None:
        path, allpaths = binary_tree_paths(root.left, path, allpaths)
    else:
        allpaths = allpaths + [path]
    if root.right is not None:
        path, allpaths = binary_tree_paths(root.right, path, allpaths)
    else:
        allpaths = allpaths + [path]
    return path, allpaths

node5 = Node(5)
node2 = Node(2, None, node5)
node3 = Node(3)
node1 = Node(1, node2, node3)


