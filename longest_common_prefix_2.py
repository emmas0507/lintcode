class Queue(object):
    def __init__(self):
        self.q = []
    def empty(self):
        return len(self.q) == 0
    def pop(self):
        if not self.empty():
            x = self.q[0]
            self.q = self.q[1:]
            return x
        else:
            return None
    def push(self, x):
        self.q = self.q + [x]

def longest_common_prefix_2(string_list, target):
    max_len = -1
    valid_queue = Queue()
    for i in range(len(string_list)):
        valid_queue.push(i)
    while not valid_queue.empty():
        max_len = max_len + 1
        tmp = Queue()
        while not valid_queue.empty():
            curr = valid_queue.pop()
            if string_list[curr][max_len] == target[max_len]:
                tmp.push(curr)
        valid_queue = tmp
    return max_len

string_list = ["abcba","acc","abwsf"]

target = "abse"

print(longest_common_prefix_2(string_list, target))
