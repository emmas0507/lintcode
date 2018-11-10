class Stack(object):
    def __init__(self):
        self.alist = []

    def push(self, x):
        self.alist = self.alist + [x]

    def top(self):
        if len(self.alist) < 1:
            return None
        else:
            return self.alist[-1]

    def pop(self):
        if len(self.alist) > 0:
            x = self.alist[-1]
            self.alist = self.alist[:-1]
            return x
        else:
            return None

class MaxStack(object):
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)
        if self.s2.top() <= x:
            self.s2.push(x)

    def top(self):
        return self.s1.top()

    def pop(self):
        return self.s1.pop()

    def popMax(self):
        x = self.s2.top()
        s = Stack()
        while self.s1.top() != self.s2.top():
            s.push(self.s1.top())
            self.s1.pop()
        self.s1.pop()
        self.s2.pop()
        while s.top() is not None:
            self.push(self.s.pop())
        return x

    def peekMax(self):
        return self.s2.top()


ms = MaxStack()
ms.push(5)
ms.push(1)
ms.push(5)
print(ms.top())
print(ms.popMax())
print(ms.top())
print(ms.peekMax())
print(ms.pop())
print(ms.top())

