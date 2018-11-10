# get the first position of target (int) in a sorted array

def first_position_target(alist, target):
    head = 0
    tail = len(alist)-1
    while head < tail - 1:
        mid = (head + tail) // 2
        if alist[mid] < target:
            head = mid
        elif alist[mid] >= target:
            tail = mid

    if alist[head] == target:
        return head
    elif alist[tail] == target:
        return tail
    else:
        return -1

alist = [1,2,3,3,4,5,10]
target = 3
print(first_position_target(alist, target))


