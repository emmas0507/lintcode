def binary_tree_level_order_travesral(atree):
    level_list = [atree]
    tmp_list = []
    while len(level_list) > 0:
        for curr_node in level_list:
            if curr_node is not None:
                tmp_list = tmp_list + [curr_node.left, curr_node.right]
        if len(level_list) > 0:
            print([x.value for x in level_list if x is not None])
        level_list = tmp_list
        tmp_list = []


class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

node15 = Node(15, None, None)
node7 = Node(7, None, None)
node20 = Node(20, node15, node7)
node9 = Node(9, None, None)
node3 = Node(3, node9, node20)

print(binary_tree_level_order_travesral(node3))
