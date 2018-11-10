def merge_sorted_list(list_of_interval):

    list_of_interval = sorted(list_of_interval, key=lambda x: x[0])
    current_upper = list_of_interval[0][1]
    merged_interval = [list_of_interval[0]]
    for interval_ in list_of_interval[1:]:
        if interval_[0] > current_upper:
            merged_interval = merged_interval + [interval_]
            current_upper = interval_[1]
        elif interval_[1] > current_upper:
            merged_interval[-1] = [merged_interval[-1][0], interval_[1]]
            current_upper = interval_[1]
        else:
            pass
        print(merged_interval)
    return merged_interval

list_of_interval = [[2, 6], [1, 3], [15, 18], [8, 10]]

print(merge_sorted_list(list_of_interval))

