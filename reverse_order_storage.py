class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_order_storage(head, alist):
    if head is None:
        index = -1
        return index, alist
    else:
        index, alist = reverse_order_storage(head.next, alist)
        index = index + 1
        alist[index] = head.value
    return index, alist

node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)
alist = [None] * 3
index, alist = reverse_order_storage(node1, alist)
print(alist)
