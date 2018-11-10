class Stack(object):
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s = self.s + [x]

    def empty(self):
        return len(self.s) == 0

    def pop(self):
        if not self.empty():
            x = self.s[-1]
            self.s = self.s[:-1]
            return x
        else:
            return None

    def peek(self):
        if not self.empty():
            return self.s[-1]
        else:
            return None

class Queue(object):
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)

    def peek(self):
        while not self.s1.empty():

            self.s2.push(self.s1.pop())
        self.s1 = self.s2
        return self.s1.peek()

    def pop(self):
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        import pdb; pdb.set_trace()
        self.s1 = self.s2
        self.s2 = Stack()
        return self.s1.pop()

q = Queue()
q.push(1)
q.push(2)
print(q.pop())
print(q.pop())
