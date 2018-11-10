def move_zeros(alist):
    i = 0
    for j in range(len(alist)):
        if alist[j] != 0:
            tmp = alist[i]
            alist[i] = alist[j]
            alist[j] = tmp
            i = i + 1
    return alist

alist = [0, 1, 0, 3, 12]
print(move_zeros(alist))

