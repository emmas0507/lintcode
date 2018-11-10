class Queue(object):
    def __init__(self):
        self.q = []

    def push(self, value):
        self.q = self.q + [value]

    def size(self):
        return len(self.q)

    def empty(self):
        return len(self.q) == 0

    def pop(self):
        if not self.empty():
            x = self.q[0]
            self.q = self.q[1:]
            return x
        else:
            print('queue is empty')
            return None

class Stack(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q1.push(value)

    def empty(self):
        return self.q1.empty()

    def pop(self):
        if self.empty():
            print('stack is empty')
        else:
            while self.q1.size() > 1:

                self.q2.push(self.q1.pop())
            q = self.q1.pop()
            self.q2.push(q)
            tmp = self.q1
            self.q1 = self.q2
            self.q2 = tmp
            return q

    def top(self):
        if self.empty():
            print('stack is empty')
        else:
            while self.q1.size > 1:
                self.q2.push(self.q1.pop())
            q = self.q1.pop()

            tmp = self.q1
            self.q1 = self.q2
            self.q2 = tmp
            return q

s1 = Stack()
s1.push(1)
s1.push(2)
print(s1.pop())
s1.push(3)
s1.push(4)
print(s1.pop())
