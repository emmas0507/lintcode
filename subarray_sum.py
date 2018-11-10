def subarray_sum(input_array, target):
    sum_dict = {}
    sum_ = 0
    index_list = []
    for i in range(len(input_array)):
        sum_ = sum_ + input_array[i]
        print('i is {}, sum_ is {}'.format(i, sum_))
        if sum_ == target:
            index_list = index_list + [(0, i)]
        elif (sum_ - target) in sum_dict.keys():
            index_list = index_list + [[sum_dict[sum_ - target]+1, i]]
        elif ((target - sum_) in sum_dict.keys()):
            index_list = index_list + [[sum_dict[target - sum_]+1, i]]
        else:
            sum_dict[sum_] = i
    if len(index_list) > 0:
        return index_list
    else:
        return None

input_array = [-3, 1, 2, -3, 4]
target = 0

print(subarray_sum(input_array, target))
