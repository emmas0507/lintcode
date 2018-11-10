def majority_number(alist):
    dict = {}
    for value in alist:
        if value in dict.keys():
            dict[value] = dict[value] + 1
        else:
            dict[value] = 1
    count_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return count_list[0][1]

alist = [1, 1, 1, 1, 2, 2, 2]

print(majority_number(alist))
