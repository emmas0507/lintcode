def insert_interval(interval_list, an_interval):
    if an_interval[1] < interval_list[0][0]:
        return [an_interval] + interval_list

    index = 0
    while index < len(interval_list) and interval_list[index][1] < an_interval[0]:
        index = index + 1
    start_index = index
    print(start_index)
    if start_index == len(interval_list):  # not in the range of interval_list
        return interval_list + [an_interval]

    end_index = start_index
    while end_index < len(interval_list):
        print(end_index)
        if interval_list[end_index][0] > an_interval[1]:  # no overlap
            return interval_list[:start_index-1] + [an_interval] + interval_list[end_index:]
        else:
            an_interval = (min(interval_list[end_index][0], an_interval[0]), max(interval_list[end_index][1], an_interval[1]))
            end_index = end_index + 1
            print(an_interval)

    if start_index < 1:
        return [an_interval] + interval_list[end_index:]
    else:
        return interval_list[:start_index] + [an_interval] + interval_list[end_index:]

import sys

def insert_interval(interval_list, an_interval):
    interval_list = [(-sys.maxint, -sys.maxint)] + interval_list + [(sys.maxint, sys.maxint)]

    index = 0
    while index < len(interval_list) and interval_list[index][1] < an_interval[0]:
        index = index + 1
    start_index = index
    print(start_index)

    end_index = start_index
    while end_index < len(interval_list):
        print(end_index)
        if interval_list[end_index][0] > an_interval[1]:  # no overlap
            return interval_list[:start_index] + [an_interval] + interval_list[end_index:]
        else:
            an_interval = (min(interval_list[end_index][0], an_interval[0]), max(interval_list[end_index][1], an_interval[1]))
            end_index = end_index + 1
            print(an_interval)

interval_list = [(1, 2), (5, 9)]
an_interval = (3, 4)

print(insert_interval(interval_list, an_interval))





