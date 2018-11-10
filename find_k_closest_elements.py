def find_k_closet_elements(sorted_list, target, k):
    start = 0
    end = len(sorted_list) - 1
    while start < end - 1:
        mid = (start + end) / 2
        if sorted_list[mid] < target:
            start = mid
        elif sorted_list[mid] > target:
            end = mid
        else:
            break
    if abs(sorted_list[start] - target) <= abs(sorted_list[mid] - target) and abs(sorted_list[start] - target) <= abs(sorted_list[end] - target):
        closest = start
    elif abs(sorted_list[mid] - target) < abs(sorted_list[start] - target) and abs(sorted_list[mid] - target) <= abs(sorted_list[end] - target):
        closest = mid
    else:
        closest = end

    start_k = closest
    end_k = closest
    print('closest index is {}'.format(closest))
    while (end_k - start_k + 1) < k:
        if start_k > 0 and end_k < len(sorted_list) - 1:
            if abs(sorted_list[start_k-1] - target) <= abs(sorted_list[end_k+1] - target):
                start_k = start_k - 1
            else:
                end_k = end_k + 1
        elif start_k > 0:
            start_k = start_k - 1
        else:
            end_k = end_k + 1
        print('start_k and end_k are {}, {}'.format(start_k, end_k))

    return sorted_list[start_k:(end_k + 1)]

sorted_list = [1,2,3,4,5]
k = 4
x = -1

print(find_k_closet_elements(sorted_list, x, k))
