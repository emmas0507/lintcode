def reach_a_number(k):
    sum = 0
    i = 1
    while True:
        sum = sum + i
        if sum >= k:
            break
        i = i + 1
    step_lists = range(1, i+1)
    if (sum - k) % 2 == 0:
        rev_index = (sum - k) / 2 - 1
        if rev_index >= 0:
            step_lists[rev_index] = -step_lists[rev_index]
    else:
        i = i + 1
        step_lists = step_lists + [i]
        sum = sum + i
        if (sum - k) % 2 == 0:
            rev_index = (sum - k) / 2 - 1
            step_lists[rev_index] = -step_lists[rev_index]
        else:
            i = i + 1
            step_lists = step_lists + [i]
            sum = sum + i
            if (sum - k) % 2 == 0:
                rev_index = (sum - k) / 2 - 1
                step_lists[rev_index] = -step_lists[rev_index]
    return step_lists

k = 4
print(reach_a_number(k))
k = 5
print(reach_a_number(k))
