def delete_node(head, target):
    while head.next is not None and head.next.value != target:
        head = head.next
    head.next = head.next.next

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_list(head):
    while head is not None:
        print('curr node is {}'.format(head.value))
        head = head.next

node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

delete_node(node1, target=3)

print_list(node1)

