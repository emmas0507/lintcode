class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def convert_sorted_array(input_array):
    print('input_array: {}'.format(input_array))
    if len(input_array) == 0:
        return None
    elif len(input_array) == 1:
        node = Node(input_array[0], left=None, right=None)
        return node
    else:
        mid = (len(input_array)) // 2
        node = Node(input_array[mid], left=convert_sorted_array(input_array[:mid]), right=convert_sorted_array(input_array[(mid+1):]))
        return node

def print_tree(root):
    cur_level = [root]
    next_level = []
    while len(cur_level) > 0:
        print('this level:')
        for n in cur_level:
            print(n.value)
            if n.left is not None:
                next_level = next_level + [n.left]
            if n.right is not None:
                next_level = next_level + [n.right]
        cur_level = next_level
        next_level = []

node1 = Node(1)
node3 = Node(3)
node5 = Node(5)
node7 = Node(7)
node2 = Node(2, node1, node3)
node6 = Node(6, node5, node7)
node4 = Node(4, node2, node6)

# print_tree(node4)

# input_array = [1, 2, 3, 4, 5, 6, 7]
input_array = [1,2,3,4]
tree = convert_sorted_array(input_array)
print_tree(tree)

