def valid_perfect_square(n):
    head = 0
    tail = n
    while head < tail - 1:

        mid = (head + tail) / 2
        print('head, mid and tail: {}, {}, {}'.format(head, mid, tail))
        if mid * mid == n:
            return True
        elif mid * mid < n:
            head = mid
        else:
            tail = mid
    if (head * head == n) or (mid * mid == n) or (tail * tail == n):
        return True
    else:
        return False

print(valid_perfect_square(169))
