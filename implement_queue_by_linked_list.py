class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class queue(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        if self.head is not None:
            h = self.head
            self.head = h.next
            if self.head is None:
                self.tail = None
            return h
        else:
            print('queue is empty')

q = queue()
node1 = Node(1)
q.add(node1)
node2 = Node(2)
q.add(node2)
print('pop first element: {}'.format(q.pop().value))

print('queue first element is {}'.format(q.head.value))
print('pop first element: {}'.format(q.pop().value))
print('pop first element: {}'.format(q.pop()))
