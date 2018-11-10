def remove_n_node(linked_list, n):
    header = linked_list
    node = linked_list
    for i in range(n+1):
        node = node.next
    print('node is {}'.format(node.value))
    print('header is {}'.format(header.value))
    while node is not None:
        header = header.next
        node = node.next
    header.next = header.next.next
    return linked_list

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node5 = Node(5)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

def print_linked_list(head):
    while head is not None:
        print(head.value)
        head = head.next

new_list = remove_n_node(node1, n=2)
print_linked_list(new_list)
