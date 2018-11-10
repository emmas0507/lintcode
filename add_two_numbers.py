def add_two_numbers(lista, listb):
    added_list = Node(None)
    tail = added_list
    increase_value = 0
    while (lista is not None) and (listb is not None):
        value = lista.value + listb.value + increase_value
        print('value is {}'.format(value))
        if value >= 10:
            new_value = value - 10
            tail.next = Node(new_value)
            tail = tail.next
            increase_value = 1
        else:
            new_value = value
            tail.next = Node(new_value)
            tail = tail.next
            increase_value = 0
        lista = lista.next
        listb = listb.next

    if lista is None:
        left_list = listb
    elif listb is None:
        left_list = lista
    else:
        left_list = None

    if left_list is None and increase_value == 0:
        return added_list
    elif left_list is None and increase_value > 0:
        tail.next = Node(increase_value)
        tail = tail.next
    elif left_list is not None:
        while left_list is not None:
            value = increase_value + left_list.value
            if value > 10:
                tail.next = Node(value-10)
                tail = tail.next
                increase_value = 1
            else:
                tail.next = Node(value)
                tail = tail.next
                increase_value = value
    if increase_value > 0:
        tail.next = Node(increase_value)
        tail = tail.next
    return added_list

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_list(list):
    while list is not None:
        print(list.value)
        list = list.next

# node6 = Node(6)
# node1 = Node(1, node6)
# lista = Node(7, node1)
#
# node2 = Node(2)
# node9 = Node(9, node2)
# listb = Node(5, node9)

node5 = Node(5)
node1 = Node(1, node5)
node3 = Node(3, node1)
lista = node3

node2 = Node(2)
node9 = Node(9, node2)
node52 = Node(5, node9)
listb = node52

print_list(add_two_numbers(lista, listb))




