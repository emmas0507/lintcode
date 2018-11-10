def insert_binary_search_tree(tree, new_node):
    if new_node.value < tree.value:
        if tree.left is None:
            tree.left = new_node
            return None
        else:
            insert_binary_search_tree(tree.left, new_node)
    else:
        if tree.right is None:
            tree.right = new_node
            return None
        else:
            insert_binary_search_tree(tree.right, new_node)

def print_tree_preorder(tree):
    if tree is None:
        return None
    print_tree_preorder(tree.left)
    print(tree.value)
    print_tree_preorder(tree.right)

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_binary_search_tree(tree, new_node):
    # do not use recursive
    parent = tree
    while parent is not None:
        if new_node.value < parent.value:
            if parent.left is None:
                parent.left = new_node
                parent = None
            else:
                parent = parent.left
        else:
            if parent.right is None:
                parent.right = new_node
                parent = None
            else:
                parent = parent.right

node3 = Node(3)
node4 = Node(4, node3)
node1 = Node(1)
node2 = Node(2, node1, node4)

node6 = Node(6)
# print_tree_preorder(node2)
insert_binary_search_tree(node2, node6)
print_tree_preorder(node2)

