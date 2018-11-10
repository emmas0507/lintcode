def search_insert(alist, target):
    head = 0
    tail = len(alist)-1
    while head < tail - 1:
        print('head is {}'.format(head))
        print('tail is {}'.format(tail))
        mid = (head + tail) // 2
        if alist[mid] < target:
            head = mid
        elif alist[mid] > target:
            tail = mid
        else:
            return mid

    print('{}, {}, {}'.format(head, tail, mid))
    if alist[head] >= target:
        return head
    elif alist[tail] >= target:
        return tail
    else:
        return tail + 1


alist = [1, 3, 5, 7]
target = 8
print(search_insert(alist, target))
