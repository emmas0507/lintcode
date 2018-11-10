class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def compare_two_tree(a_root, b_root):
    if a_root is not None:
        avalue = a_root.value
    else:
        avalue = None
    if b_root is not None:
        bvalue = b_root.value
    else:
        bvalue = None
    print('compare two tree {}, {}'.format(avalue, bvalue))
    if a_root is None and b_root is None:
        print('a_root is None and b_root is None')
        return True
    elif a_root is not None and b_root is None:
        print('a_root is {} and b_root is None'.format(a_root.value))
        return False
    elif a_root is None and b_root is not None:
        print('a_root is None and b_root is {}'.format(b_root.value))
        return False
    elif a_root.value != b_root.value:
        print('a_root is {}, b_root is {}'.format(a_root.value, b_root.value))
        return False
    else:
        curr_ = a_root.value == b_root.value
        left_ = compare_two_tree(a_root.left, b_root.left)
        right_ = compare_two_tree(a_root.right, b_root.right)
        print('curr {}, left_ {}, right {}'.format(curr_, left_, right_))
        return (curr_ and left_ and right_)

def subtree(parent_root, child_root):
    curr_ = compare_two_tree(parent_root, child_root)
    if curr_ is True:
        return True
    else:
        left_ = compare_two_tree(parent_root.left, child_root)
        if left_ is True:
            return True
        else:
            right_ = compare_two_tree(parent_root.right, child_root)
            if right_ is True:
                return True
    return False

node4 = Node(4)
node2 = Node(2)
node3 = Node(3, node4, None)
node1 = Node(1, node2, node3)

node44 = Node(4)
node33 = Node(3, None, node44)

print(subtree(node1, node33))
