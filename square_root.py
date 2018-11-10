def square_root(x):
    head = 0
    tail = x
    mid = (head + tail) // 2

    while mid >= 0 and mid <= x:
        print('mid is {}'.format(mid))
        if mid * mid <= x:
            if (mid+1) * (mid+1) > x:
                return mid
            else:
                mid = (mid + tail + 1) // 2
        else:
            mid = (head + mid) // 2

    return None

print(square_root(10))
