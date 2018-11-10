def partition_list(alist, target):
    small_head = None
    small_tail = None
    large_head = None
    large_tail = None

    while alist is not None:
        print(alist.value)
        if alist.value < target:
            if small_head is None:
                small_head = alist
                small_tail = alist
            else:
                small_tail.next = alist
                small_tail = alist
        else:
            if large_head is None:
                large_head = alist
                large_tail = alist
            else:
                large_tail.next = alist
                large_tail = alist


        alist = alist.next

    small_tail.next = large_head
    large_tail.next = None
    return small_head

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node2 = Node(2)
node5 = Node(5, node2)
node22 = Node(2, node5)
node3 = Node(3, node22)
node4 = Node(4, node3)
node1 = Node(1, node4)

def print_list(alist):
    head = alist
    while head is not None:
        print(head.value)
        head = head.next

# print_list(node1)

new_list = partition_list(node1, target=3)

print('new list')
print_list(new_list)

