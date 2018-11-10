import numpy as np

def replace_space_with_target(s_array, origin_str=' ', replace_str='20%'):
    number_of_space = np.array([0] * len(s_array))
    tmp = 0
    for i in range(len(s_array)):
        if s_array[i] is None:
            break
        if s_array[i] == origin_str:
            tmp = tmp + 1
        number_of_space[i] = tmp
    print(number_of_space)
    j_ = i
    while j_ >= 0:
        print("j_ is {}".format(j_))
        new_index = (len(replace_str) - len(origin_str)) * number_of_space[j_] + j_
        print('new index is {}'.format(new_index))
        if s_array[j_] == origin_str:
            s_array[(new_index-2):(new_index+1)] = np.array(list(replace_str))
        else:
            s_array[new_index] = s_array[j_]
        j_ = j_ - 1
    return s_array

s_array = np.array(list('mr john') + [None, None, None, None, None, None, None])

print(replace_space_with_target(s_array))

