class node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def swap_nodes_in_pairs(head):
    head0 = node(0, head)
    head = head0
    # print_list(head)
    while head.next is not None and head.next.next is not None:
        rest_list = head.next.next.next
        head_next = head.next.next
        head_next_next = head.next
        head.next = head_next
        head_next.next = head_next_next
        head_next_next.next = rest_list
        # print_list(head)
        head = head.next.next
        # import pdb; pdb.set_trace()

    return head0.next

def print_list(head):
    print('list is: ')
    while head is not None:
        print(head.value)
        head = head.next

node4 = node(4)
node3 = node(3, node4)
node2 = node(2, node3)
node1 = node(1, node2)
node0 = node(0, node1)

print_list(swap_nodes_in_pairs(node0))
