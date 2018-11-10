def get_median(alist):
    alen = len(alist)
    if alen % 2 == 0:
        a = get_kth(alist, alen // 2 - 1)
        b = get_kth(alist, alen // 2)
        print(a)
        print(b)
        return (a + b) * 1.0 / 2
    else:
        return get_kth(alist, alen // 2)

def get_kth(alist, k):
    # choose first element as pivot, divide array into less than pivot, pivot and larger than pivot
    if len(alist) == 1:
        return alist[0]
    pivot = alist[0]
    j = 0
    for i in range(0, len(alist)):
        if alist[i] < pivot:
            tmp = alist[i]
            alist[i] = alist[j+1]
            alist[j+1] = tmp
            j = j + 1

    alist[0] = alist[j]
    alist[j] = pivot
    print(alist)
    print(j)
    print(k)
    if j < k:
        return get_kth(alist[(j+1):], k-j-1)
    elif j > k:
        return get_kth(alist[0:j], k)
    else:
        return pivot

# alist = [4, 5, 1, 2, 3]
alist = [7, 9, 4, 5]
# alist = [4,5,7,9]
# k = 3
# print(get_kth(alist, k))
print(get_median(alist))


