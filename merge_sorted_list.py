def merge_two_sorted_list(alist, blist):
    list = []
    ahead = 0
    bhead = 0
    while ahead < len(alist) and bhead < len(blist):
        if alist[ahead] <= blist[bhead]:
            list = list + [alist[ahead]]
            ahead = ahead + 1
        else:
            list = list + [blist[bhead]]
            bhead = bhead + 1
    print('ahead, bhead: {}, {}'.format(ahead, bhead))
    if ahead < len(alist):
        list = list + alist[ahead:]
    else:
        list = list + blist[bhead:]
    return list

alist = [1, 2, 4]
blist = [3, 5]
print(merge_two_sorted_list(alist, blist))
