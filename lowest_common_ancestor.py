class Node(object):
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

def print_node_list(node_list):
    for n in node_list:
        print(n.value)

def get_path(root, target):
    curr_list = [root]

    while len(curr_list) > 0:
        print('curr_list is ')
        print_node_list(curr_list)
        curr_node = curr_list[-1]
        if curr_node.value == target:
            break
        else:
            curr_list = curr_list[:(-1)]
            if curr_node.left is not None:
                curr_list = curr_list + [curr_node.left]
            if curr_node.right is not None:
                curr_list = curr_list + [curr_node.right]
    print('target node is {}'.format(curr_node.value))
    path = []
    while curr_node is not None:
        path = [curr_node.value] + path
        curr_node = curr_node.parent
    return path

def lowest_common_ancestor(root, target1, target2):
    path1 = get_path(root, target1)
    path2 = get_path(root, target2)
    print('path1 and path2 are {}, {}'.format(path1, path2))
    common_path = []
    for i in range(min(len(path1), len(path2))):
        if path1[i] == path2[i]:
            common_path = common_path + [path1[i]]
    return common_path

node5 = Node(5)
node6 = Node(6)
node3 = Node(3)
node7 = Node(7, None, node5, node6)
node4 = Node(4, None, node3, node7)

node4.parent = None
node3.parent = node4
node7.parent = node4
node5.parent = node7
node6.parent = node7

print(lowest_common_ancestor(node4, 6, 7))



