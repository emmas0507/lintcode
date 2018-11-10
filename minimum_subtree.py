class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def minimum_subtree(root):
    if root.left is not None:
        left_min_sum, left_min_node, left_sum = minimum_subtree(root.left)
    else:
        left_min_sum = 10000
        left_min_node = None
        left_sum = 0
    if root.right is not None:
        right_min_sum, right_min_node, right_sum = minimum_subtree(root.right)
    else:
        right_min_sum = 10000
        right_min_node = None
        right_sum = 0
    import pdb; pdb.set_trace()
    if root.value + left_sum + right_sum <= left_min_sum and root.value + left_sum + right_sum <= right_min_sum:
        return root.value + left_sum + right_sum, root, root.value + left_sum + right_sum
    elif left_min_sum < root.value + left_sum + right_sum and left_min_sum <= right_min_sum:
        return left_min_sum, left_min_node, root.value + left_sum + right_sum
    else:
        return right_min_sum, right_min_node, root.value + left_sum + right_sum

node0 = Node(0)
node2 = Node(2)
node_4 = Node(-4)
node_5 = Node(-5)
node_52 = Node(-5, node0, node2)
node22 = Node(2, node_4, node_5)
node1 = Node(1, node_52, node22)

min_sum, node, sum_ = minimum_subtree(node1)
print(min_sum, node.value, sum_)
