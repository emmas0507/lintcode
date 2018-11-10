class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_list(header):
    while header is not None:
        print(header.value)
        header = header.next

def insertion_sort_list(input_list):
    new_list = Node(-float('inf'))
    curr_node = input_list
    while curr_node is not None:
        value = curr_node.value
        header = new_list
        # import pdb; pdb.set_trace()
        while header is not None:
            if header.value < value and (header.next is None or header.next.value >= value):
                insert_node = Node(value)
                insert_node.next = header.next
                header.next = insert_node
                break
            else:
                header = header.next
        curr_node = curr_node.next
        # print('curr_node is {}'.format(value))
        # print_list(new_list)
    return new_list.next

node0 = Node(0)
node2 = Node(2, node0)
node3 = Node(3, node2)
node1 = Node(1, node3)

print_list(insertion_sort_list(node1))

