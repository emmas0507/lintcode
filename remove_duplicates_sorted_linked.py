def remove_duplicates_sorted_linked(header):
    new_list_tail = header
    tail = header.next
    current_value = header.value
    while tail is not None:
        if (current_value is None) or (tail.value > current_value):
            current_value = tail.value
            new_list_tail.next = tail
            new_list_tail = tail
            tail = tail.next
        else:
            tail = tail.next
    new_list_tail.next = None
    return header

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_list(header):
    while header is not None:
        print(header.value)
        header = header.next


node2 = Node(2)
node13 = Node(1, node2)
node12 = Node(1, node13)
node11 = Node(1, node12)

# print_list(node11)

print('updated list')
new_list = remove_duplicates_sorted_linked(node11)
print_list(new_list)

