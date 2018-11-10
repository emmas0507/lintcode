class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_list(header):
    while header is not None:
        print(header.value)
        header = header.next

def plus_one_linked_list(header):
    reverse_linked_list = None
    while header is not None:
        new_node = Node(header.value, reverse_linked_list)
        reverse_linked_list = new_node
        header = header.next

    add = 1
    reverse_head = reverse_linked_list
    while reverse_head is not None:
        updated_value = add + reverse_head.value
        if updated_value < 10:
            reverse_head.value = updated_value
            break
        else:
            reverse_head.value = 0
            add = 1
            reverse_head = reverse_head.next

    # reverse linked list
    updated_list = None
    while reverse_linked_list is not None:
        new_node = Node(reverse_linked_list.value, updated_list)
        updated_list = new_node
        reverse_linked_list = reverse_linked_list.next

    if updated_value == 10:
        new_node = Node(1, updated_list)

    updated_list = new_node
    return updated_list

node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)

node9 = Node(9)
node99 = Node(9, node9)
node999 = Node(9, node99)

new_list = plus_one_linked_list(node999)
print_list(new_list)
