def balance_tree(tree):
    def balance_tree(tree):
        # tell if a tree is balanced, for any node,
        # length of left node and length of right node less or equal than 1
        if tree is None:
            return (0, True)
        else:
            left_height = balance_tree(tree.left)
            right_height = balance_tree(tree.right)
            node_height = max(left_height[0], right_height[0]) + 1
            print(tree.value)
            print(node_height)
            balance_flag = abs(left_height[0] - right_height[0]) <= 1
            balance_flag = (left_height[1] & right_height[1]) & balance_flag
            print(balance_flag)
            return (node_height, balance_flag)
    (height, balance_flag) = balance_tree(tree)
    return balance_flag

class node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

node15 = node(15, None, None)
node7 = node(7, None, None)
node20 = node(20, node15, node7)
node3 = node(3, None, node20)

print(balance_tree(node3))



