# reverse linked list

class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def set_next_node(self, input_node):
        self.next = input_node

def reverse_linked_list(linked_list):
    head = linked_list
    new_list = None
    while head is not None:
        value = head.value
        new_node = Node(value)
        new_node.set_next_node(new_list)
        new_list = new_node
        head = head.next
    return new_list

def print_linked_list(head):
    while head is not None:
        print head.value
        head = head.next

node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)

print_linked_list(node1)

reverse_list = reverse_linked_list(node1)

print_linked_list(reverse_list)
