class Stack(object):
    def __init__(self):
        self.s = []

    def empty(self):
        return len(self.s) == 0

    def push(self, x):
        self.s = self.s + [x]

    def pop(self):
        if not self.empty():
            x = self.s[-1]
            self.s = self.s[:-1]
            return x

def input_stream(input1, input2):
    stack1 = Stack()
    stack2 = Stack()
    for i in input1:
        if i != '<':
            stack1.push(i)
        else:
            stack1.pop()
    for i in input2:
        if i != '<':
            stack2.push(i)
        else:
            stack2.pop()
    l1 = stack1.pop()
    l2 = stack2.pop()
    return l1 == l2

input1 = 'abcde<<'
input2 = 'abcd<e<'

print(input_stream(input1, input2))
