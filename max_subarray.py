# max subarray

def max_subarray(alist):
    max_sub = [0] * len(alist)
    max_sub[0] = alist[0]
    for i in range(1, len(alist)):
        if max_sub[i-1] <= 0:
            max_sub[i] = alist[i]
        else:
            max_sub[i] = max_sub[i-1] + alist[i]
    # return max_sub
    return max(max_sub)

alist = [-2, 2, -3, 4, -1, 2, 1, -5, 3]

print(max_subarray(alist))



