def two_sum(alist, target):
    dict_index = {}
    for i in range(len(alist)):
        if alist[i] in dict_index.keys():
            dict_index[alist[i]] = dict_index[alist[i]] + [i]
        else:
            dict_index[alist[i]] = [i]
    print(dict_index)
    value_lists = dict_index.keys()
    for v in value_lists:
        v2 = target - v
        if v2 in dict_index.keys():
            if v2 != v:
                index1 = dict_index[v][0]
                index2 = dict_index[v2][0]
                break
            else:
                if len(dict_index[v]) >= 2:
                    index1 = dict_index[v][0]
                    index2 = dict_index[v][1]
                    break
    index_list = sorted([index1, index2])
    return index_list

numbers = [2, 7, 4, 15]
target = 9
print(two_sum(numbers, target))
