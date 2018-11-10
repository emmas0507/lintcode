def triangle(root):
    if root is None:
        return 0
    else:
        return min(triangle(root.left), triangle(root.right)) + root.value

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

node4 = Node(4)
node1 = Node(1)
node8 = Node(8)
node3 = Node(3)
node6 = Node(6, node4, node1)
node5 = Node(5, node1, node8)
node7 = Node(7, node8, node3)
node32 = Node(3, node6, node5)
node42 = Node(4, node5, node7)
node2 = Node(2, node32, node42)

print(triangle(node2))
