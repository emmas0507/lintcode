def last_position_of_target(sorted_list, target):
    start = 0
    end = len(sorted_list) - 1

    while start < end - 1:
        mid = (start + end) / 2
        if sorted_list[mid] > target:
            end = mid
        else:
            start = mid

    if sorted_list[end] == target:
        return end
    elif sorted_list[mid] == target:
        return mid
    elif sorted_list[start] == target:
        return start
    else:
        return None

sorted_list = [1,2,2,4,5,5]
sorted_list = [2,2,2,2,2,2]
target = 2
print(last_position_of_target(sorted_list, target))



